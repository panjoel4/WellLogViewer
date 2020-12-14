from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d, LinearAxis, SingleIntervalTicker
from bokeh.io import show, output_notebook, curdoc
from bokeh.layouts import gridplot
import random

import lasio
import numpy as np
from bokeh.models.tools import PanTool, ResetTool, WheelZoomTool, HoverTool

class lasViewer:
    def __init__(self, lasname):
        self.lasname=lasname
        las = lasio.read(str(self.lasname))
        df=las.df()
        df_drop=df.dropna()
        df_reset=df_drop.reset_index()
        curvename=las.curves.keys()
        units=[]
        for i in range (len(curvename)):
            units.append((las.curves["%s" %curvename[i]].unit ))
        figDict={}
        unitDict=dict(zip(curvename,units))
        plotlist=[]
        print ('Log list: '+ str (curvename))
        self.version, self.well, self.curves, self.params, self.other=las.version, las.well, las.curves, las.params, las.other
        self.df, self.las, self.curvename, self.units, self.figDict, self.unitDict, self.plotlist=df_reset, las, curvename, units, figDict, unitDict, plotlist
    
    def addplot(self, curve, *args):
        TOOLTIPS = [
        ("(curve)", "($name)"),
        ("(value)", "($x)")]
        logIndex=len(self.plotlist)
        r = lambda: random.randint(0,255)
        colr='#{:02x}{:02x}{:02x}'.format(r(), r(), r())
        if self.unitDict[curve] in ('ohmm', 'OHMM'):
            self.figDict["fig{0}".format(logIndex)]=figure(x_axis_type="log", x_axis_location='above')
        else:
            self.figDict["fig{0}".format(logIndex)] = figure(tooltips=TOOLTIPS, x_axis_location='above')
        # Define 1st LHS y-axis
        self.figDict["fig{0}".format(logIndex)].yaxis.axis_label = str(self.curvename[0])+' (' + str(self.unitDict[self.curvename[0]])+ ')'
        self.figDict["fig{0}".format(logIndex)].y_range = Range1d(start=max(self.df[self.curvename[0]]), end=min(self.df[self.curvename[0]]),  bounds=(None,None))
        unittes=[]
        # Define x-axis
        self.figDict["fig{0}".format(logIndex)].xaxis.axis_label = str(curve) + ' ('+ str(self.unitDict[curve])+')'
        self.figDict["fig{0}".format(logIndex)].x_range = Range1d(start=min(self.df[curve]), end=max(self.df[curve]))
        #fig.xaxis.ticker=SingleIntervalTicker(interval=30)
        self.figDict["fig{0}".format(logIndex)].xaxis.axis_label_text_color = colr
        # Define x-axis curve
        self.figDict["fig{0}".format(logIndex)].line(
            y = self.df[self.curvename[0]],
            x = self.df[curve],
            name = str(curve),
            color = colr
            )
        for curves in args:
            colr='#{:02x}{:02x}{:02x}'.format(r(), r(), r())
            #add more x-axis
            self.figDict["fig{0}".format(logIndex)].extra_x_ranges [str(curves)] = Range1d(start=min(self.df[curves]), end=max(self.df[curves]))
            self.figDict["fig{0}".format(logIndex)].add_layout(LinearAxis( x_range_name=curves, 
                                      axis_label=str(curves) + ' ('+ str(self.unitDict[curves])+')', axis_label_text_color = colr), 'above')

            # Define other x-axis curve
            self.figDict["fig{0}".format(logIndex)].line(
                y = self.df[self.curvename[0]],
                x = self.df[curves],
                name = curves,
                x_range_name = str(curves),
                color = colr
            )
        self.plotlist.append(self.figDict["fig{0}".format(logIndex)])
        self.figDict["fig{0}".format(logIndex)].tools=[WheelZoomTool(),PanTool(),ResetTool()]
        self.figDict["fig{0}".format(logIndex)].add_tools(HoverTool(tooltips=TOOLTIPS))
        return self.figDict["fig{0}".format(logIndex)]
    
    def header(self):
        print (self.version)
        print (self.well)
        print (self.curves)
        print (self.params)
        print (self.other)
