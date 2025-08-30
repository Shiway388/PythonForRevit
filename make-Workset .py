"""Create Workset from a list and set default visibility"""
from Autodesk.Revit import DB

def create_workset(doc, names):
    for name in names:
        ws = DB.Workset.Create(doc, name)
        if "Hidden" in name:
            set_workset_defalt_visiblity (d , ws, False)
        print("Created Workset: ", ws.Name)

# List of worksets to be created
    wdvs = DB.WorksetVisibilitySettings .GetWorksetVisibilitySettings(doc)
    wdvs .SetWorksetVisibility(DB.Workset . Id, state)


workset_names = ["Column", "Beam", "Wall", "Floor", "Roof", "Curtain Wall", "Generic Model"]

# Start transaction
if DB.WorksetTable.IsWorksetNameUnique(doc, "Test"):   # just a check, prevents duplicate errors
    t = DB.Transaction(doc, "Create Worksets")
    t.Start()
    create_workset(doc, workset_names)
    t.Commit()
