def json_2_column_graphic(heading, q_30_project_lane,q_30_media_lane):
    data_source = {}
    
    # Chart data is passed to the `dataSource` parameter, as hashes, in the form of
    # key-value pairs.
    data_source['chart'] = { 
        "caption": heading,
        "xAxisname": "Lanes",
        "yAxisName": " Q 30 (In %)",
        "numberPrefix": "%",
        "plotFillAlpha": "80",
        "paletteColors": "#0075c2,#1aaf5d",
        "baseFontColor": "#333333",
        "baseFont": "Helvetica Neue,Arial",
        "captionFontSize": "14",
        "subcaptionFontSize": "14",
        "subcaptionFontBold": "0",
        "showBorder": "0",
        "bgColor": "#ffffff",
        "showShadow": "0",
        "canvasBgColor": "#ffffff",
        "canvasBorderAlpha": "0",
        "divlineAlpha": "100",
        "divlineColor": "#999999",
        "divlineThickness": "1",
        "divLineIsDashed": "1",
        "divLineDashLen": "1",
        "divLineGapLen": "1",
        "usePlotGradientColor": "0",
        "showplotborder": "0",
        "valueFontColor": "#ffffff",
        "placeValuesInside": "1",
        "showHoverEffect": "1",
        "rotateValues": "1",
        "showXAxisLine": "1",
        "xAxisLineThickness": "1",
        "xAxisLineColor": "#999999",
        "showAlternateHGridColor": "0",
        "legendBgAlpha": "0",
        "legendBorderAlpha": "0",
        "legendShadow": "0",
        "legendItemFontSize": "10",
        "legendItemFontColor": "#666666",
        "exportEnabled": "1"
    }
    data_source["categories"] = [
        {"category": [
                { "label": "Lane 1"},
                { "label": "Lane 2"},
                { "label": "Lane 3"},
                { "label": "Lane 4"}
            ]
        }
    ]
    data_source ["dataset"] = [
        {"seriesname": "Researcher Project",
            "data": [ 
                    {"value": q_30_project_lane[0] },
                    {"value": q_30_project_lane[1] },
                    {"value": q_30_project_lane[2] },
                    {"value": q_30_project_lane[3] }
            ]
        },
        {"seriesname": "Average for all Projects",
            "data": [
                    {"value": q_30_media_lane[0]},
                    {"value": q_30_media_lane[1]},
                    {"value": q_30_media_lane[2]},
                    {"value": q_30_media_lane[3]}
            ]
        }
    ]
    data_source["trendlines"] = [
        {"line": [
                {   "startvalue": "12",
                    "color": "#0075c2",
                    "displayvalue": "Researcher{br}Average",
                    "valueOnRight": "1",
                    "thickness": "1",
                    "showBelow": "1",
                    "tooltext": "Previous year quarterly target  : 75%"
                },
                {
                    "startvalue": "25",
                    "color": "#1aaf5d",
                    "displayvalue": "All Project{br}Average",
                    "valueOnRight": "1",
                    "thickness": "1",
                    "showBelow": "1",
                    "tooltext": "Current year quarterly target  : $23K"
                }
            ]
        }
    ]
    return data_source

def json_unknow_barcode_graphic (heading, barcode_seq, barcode_value) :
    data_source = {}
    
    # Chart data is passed to the `dataSource` parameter, as hashes, in the form of
    # key-value pairs.
    data_source['chart'] = { 
        "caption": heading,
        "subcaption": "Top Sequence found in the Run",
        "startingangle": "120",
        "showlabels": "0",
        "showlegend": "1",
        "enablemultislicing": "0",
        "slicingdistance": "15",
        "showpercentvalues": "1",
        "showpercentintooltip": "0",
        "plottooltext": "Sequence : $label Total count : $datavalue",
        "theme": "ocean",
        "exportEnabled": "1"
    }
    data_source['data']= [
                    {"label": barcode_seq[0], "value": barcode_value[0]},
                    {"label": barcode_seq[1], "value": barcode_value[1]},
                    {"label": barcode_seq[2], "value": barcode_value[2]},
                    {"label": barcode_seq[3], "value": barcode_value[3]},
                    {"label": barcode_seq[4], "value": barcode_value[4]},
                    {"label": barcode_seq[5], "value": barcode_value[5]},
                    {"label": barcode_seq[6], "value": barcode_value[6]},
                    {"label": barcode_seq[7], "value": barcode_value[7]},
                    {"label": barcode_seq[8], "value": barcode_value[8]},
                    {"label": barcode_seq[9], "value": barcode_value[9]}
                    
    ]
    return data_source

def graphic_for_top_unbarcodes (heading, theme, lane_unbarcode) :
    data_source = {}
    data_source['chart'] = { 
                "caption": heading,
                "subCaption": "Found in the runs",
                "xAxisName": "Sequence",
                "yAxisName": "Number of runs",
                #"theme": "fint",
                "theme": theme,
                "numberPrefix": "",
                "placevaluesInside": "1",
                "rotatevalues": "1",
                #Showing canvas bg to apply background color
                "showCanvasBg": "1",
                #Shwoing canvas base to apply base color
                "showCanvasBase": "1",
                #Changing canvas base depth
                "canvasBaseDepth": "14",
                #Changing canvas background depth
                "canvasBgDepth": "5",
                #Changing canvas base color
                "canvasBaseColor": "#aaaaaa",
                #Changing canvas background color
                "canvasBgColor": "#eeeeee",
                "exportEnabled": "1"
            }

    data =[]
    
    for key , values in lane_unbarcode.items() :
        data_dict = {} 
        data_dict['label'] = key
        data_dict['value'] = values
        data.append(data_dict)
    data_source['data'] = data    
        
    return data_source
    
def graphic_for_library_kit (heading, sub_caption, x_axis_name, y_axis_name, theme, lane_quality) :
    data_source = {}
    data_source['chart'] = { 
                "caption": heading,
                "subCaption": sub_caption,
                "xAxisName": x_axis_name,
                "yAxisName": y_axis_name,
                #"theme": "fint",
                "theme": theme,
                "numberPrefix": "",
                "placevaluesInside": "1",
                "rotatevalues": "1",
                #Showing canvas bg to apply background color
                "showCanvasBg": "1",
                #Shwoing canvas base to apply base color
                "showCanvasBase": "1",
                #Changing canvas base depth
                "canvasBaseDepth": "14",
                #Changing canvas background depth
                "canvasBgDepth": "5",
                #Changing canvas base color
                "canvasBaseColor": "#aaaaaa",
                #Changing canvas background color
                "canvasBgColor": "#eeeeee",
                "exportEnabled": "1"
            }

    data =[]
    
    for key , values in lane_quality.items() :
        data_dict = {} 
        data_dict['label'] = key
        data_dict['value'] = values
        data.append(data_dict)
    data_source['data'] = data    
        
    return data_source
    

def pie_graphic_for_unknow_barcode (heading, theme, top_count_sequence):
    data_source = {}
    
    data_source['chart'] = { 
        "caption": heading,
        "subcaption": "Top Sequence found in the Run",
        "startingangle": "120",
        "showlabels": "0",
        "showlegend": "1",
        "enablemultislicing": "0",
        "slicingdistance": "15",
        "showpercentvalues": "1",
        "showpercentintooltip": "0",
        "plottooltext": "Sequence : $label Total count : $datavalue",
        "theme": theme,
        "exportEnabled": "1"
    }
    data =[]
    data_dict = {} 

    for key , values in top_count_sequence.items() :
        data_dict['label'] = key
        data_dict['value'] = values
        data.append(data_dict)
    data_source['data'] = data    
    
    return data_source
    
    

    
########
 #JSON para la calidad de la muestra/project/Run
########
def graphic_for_quality_angular (heading, value) :
    data_source = {}
    
    data_source ['chart'] = {
        "caption": heading,
        "lowerlimit": "0",
        "upperlimit": "100",
        "lowerlimitdisplay": "Bad",
        "upperlimitdisplay": "Good",
        "palette": "1",
        "numbersuffix": "%",
        "tickvaluedistance": "10",
        "showvalue": "0",
        # inner white radious 
        "gaugeinnerradius": "25",
        "bgcolor": "FFFFFF",
        "pivotfillcolor": "333333",
        "pivotradius": "8",
        "pivotfillmix": "333333, 333333",
        "pivotfilltype": "radial",
        "pivotfillratio": "0,100",
        "showtickvalues": "1",
        "showborder": "0"
    }
    data_source ['colorrange'] = {
        "color": [
                {"minvalue": "0", "maxvalue": "45","code": "e44a00"},
                {"minvalue": "45", "maxvalue": "75", "code": "f8bd19"},
                {"minvalue": "75", "maxvalue": "100", "code": "6baa01"}
                ]
                }
    data_source['dials'] = {
                "dial": [ {
                    "value": value,
                    "rearextension": "15",
                    # length fo the arrow
                    "radius": "50",
                    "bgcolor": "333333",
                    "bordercolor": "333333",
                    "basewidth": "8"
                    }
                ]
            }
    return data_source



