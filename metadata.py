# metadata.py
"""
File containing metadata information for WW2100 model run
"""
class UnknownFileType(BaseException):
    pass

AltScenarios = ["Ref","LowClim","HighClim","FireSuppress","UrbExpand","HighPop","FullCostUrb","EarlyReFill"]
##model_run = 'MIROC'
def define_model_run(Compare):
    import xlrd
    model_book = xlrd.open_workbook('Master File.xls')
    Case = str(model_book.sheet_by_index(0).col_values(0)[1])      #find the reference model type
    if "Ref_" in Case:
        model1 = 'Reference (MIROC)'
    elif "LowClim" in Case:  
        model1 = 'Low Climate Change (GFDL)'
    elif "FireSuppress" in Case:  
        model1 = 'Upland Fire Suppression'
    elif "HighClim" in Case:  
        model1 = 'High Climate Change (Hadley)'
    elif "UrbExpand" in Case:  
        model1 = "Relaxed Urban Expansion"
    elif "HighPop" in Case:  
        model1 = "High Population Growth"
    elif "FullCostUrb" in Case:  
        model1 = "Full Cost Urban"
    elif "EarlyReFill" in Case:  
        model1 = "Early ReFill"
    else:
        raise UnknownFileType()
    if Compare == "first":  Compare = str(model_book.sheet_by_index(0).col_values(1)[1])    #find the comparative model type
    if "Ref_" in Compare:
        model2 = 'Reference (MIROC)'
    elif "LowClim" in Compare:  
        model2 = 'Low Climate Change (GFDL)'
    elif "FireSuppress" in Compare:  
        model2 = 'Upland Fire Suppression'
    elif "HighClim" in Compare:  
        model2 = 'High Climate Change (Hadley)'
    elif "UrbExpand" in Compare:  
        model2 = "Relaxed Urban Expansion"
    elif "HighPop" in Compare:  
        model2 = "High Population Growth"
    elif "FullCostUrb" in Compare:  
        model2 = "Full Cost Urban"
    elif "EarlyReFill" in Compare:  
        model2 = "Early ReFill"
    else:
        raise UnknownFileType()
    model_run = model2 + ' minus ' + model1
    return model_run

model_run = define_model_run("first")  #run the program and get the metadata
