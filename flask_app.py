# import module
from flask import Flask, render_template, request, redirect


# create an instance of the Flask class called app
app = Flask (__name__)


# Define the routes and the queries
@app.route("/")
def home():
    title = "Getting started"
    intro = "Welcome to the team's database! You are looking at the user interface. The actual database (using the Sqlite3) is running behind the scenes through code written in Python. In a glance:"
    instructions = "The top right part of each page contains links leading to tables with information about Staff, Equipment, and Buildings. The page you are on is indicated by the grey box."
    add_entry = "To add an entry, click on the '+ Add' button found at the bottom of the table. Doing this will lead you to the appropriate form. Fill in the form and click 'Submit'. The new entry should now be seen in the appropriate table."
    edit_entry = "To edit an entry, click on the 'Edit' button on the same row as the entry to be edited. This will lead to the appropriate form filled in with the current information stored in the database. Correct the data and click 'Update Data'."
    delete_entry = "To delete an entry, click on the 'Delete' button on the same row as the entry to be deleted."
    return render_template("index.html", title = title, intro = intro, instructions = instructions, instructions2 = add_entry, instructions3 = edit_entry, instructions4 = delete_entry)


# App routes for CRUD - Staff

@app.route("/staff")
def sql_staff():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM staff''')
    msg = "staff/addstaff"
    return render_template("staff_table.html", results = results, msg = msg)


@app.route("/staff/addstaff")
def addstaff():
    return render_template("staff.html")


@app.route("/staff/insert", methods = ["POST","GET"])   # this is used when the user inserts a new record 
def sql_staffinsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        Staff_ID = request.form["Staff_ID"]
        Last_Name = request.form["Last_Name"]
        Initials = request.form["Initials"]
        Position = request.form["Position"]

        sql_edit_insert('''INSERT INTO staff (Staff_ID, Last_Name, Initials, Position) VALUES (?,?,?,?)''', (Staff_ID, Last_Name, Initials, Position)) 
    results = sql_query('''SELECT * FROM staff''')
    return render_template("staff_table.html", results = results)


@app.route("/staff/deletestaff", methods = ["POST", 'GET']) # this is used when a user deletes a record (row) from the staff table
def sql_staffdelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == "GET":
        lname = request.args.get("lname")
        init = request.args.get("initials")
        sql_delete('''DELETE FROM staff WHERE Last_Name = ? AND Initials = ?''', (lname, init))
    results = sql_query('''SELECT * FROM staff''')
    msg = "./addstaff"
    return render_template("staff_table.html", results = results, msg = msg)


@app.route("/staff/query_staffedit", methods = ["POST", "GET"]) # This is used when the user clicks on the Edit button
def sql_staffqueryedit():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == "GET":
        elname = request.args.get("elname") # e = for editing
        einitials = request.args.get("einitials")
        eresults = sql_query2('''SELECT * FROM staff WHERE Last_Name = ? AND Initials = ?''', (elname, einitials))
    results = sql_query('''SELECT * FROM staff''')
    return render_template("staff.html", eresults = eresults, results = results)


@app.route("/staff/edit", methods = ["POST", "GET"]) # This is used when the user submits an edited record
def sql_staffedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        old_Last_Name = request.form["old_Last_Name"]
        old_Initials = request.form["old_Initials"]
        Staff_ID = request.form["Staff_ID"]
        Last_Name = request.form["Last_Name"]
        Initials = request.form["Initials"]
        Position = request.form["Position"]
        sql_edit_insert('''UPDATE staff SET Staff_ID = ?, Last_Name = ?, Initials = ?, Position = ? WHERE Last_Name = ? AND Initials = ?''', (Staff_ID, Last_Name, Initials, Position, old_Last_Name, old_Initials))
    results = sql_query('''SELECT * FROM staff''')
    msg = "/staff/addstaff"
    return render_template("staff_table.html", results = results) 


# App routes for CRUD - Building details

@app.route("/building")
def sql_building():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM buildings''')
    msg = "staff/addbuilding"
    return render_template("building_table.html", results = results, msg = msg)


@app.route("/building/addbuilding")
def addbuilding():
    return render_template("buildings.html")


@app.route("/building/insert", methods = ["POST","GET"])   # this is used when the user inserts a new record 
def sql_buildinginsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        Building_ID = request.form["Building_ID"]
        Building_Name = request.form["Building_Name"]
        Section = request.form["Section"]
        Room = request.form["Room"]

        sql_edit_insert('''INSERT INTO buildings (Building_ID, Building_Name, Section, Room) VALUES (?,?,?,?)''', (Building_ID, Building_Name, Section, Room)) 
    results = sql_query('''SELECT * FROM buildings''')
    return render_template("building_table.html", results = results)


@app.route("/building/deletebuilding", methods = ["POST", 'GET']) # this is used when a user deletes a record (row) from the buildings table
def sql_buildingdelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == "GET":
        bname = request.args.get("bname")
        room = request.args.get("rm")
        sql_delete('''DELETE FROM buildings WHERE Building_Name = ? AND Room = ?''', (bname, room))
    results = sql_query('''SELECT * FROM buildings''')
    msg = "./addbuilding"
    return render_template("building_table.html", results = results, msg = msg)


@app.route("/building/query_buildingedit", methods = ["POST", "GET"]) # This is used when the user clicks on the Edit button
def sql_buildingqueryedit():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == "GET":
        ebname = request.args.get("ebname") # e = for editing
        erm = request.args.get("erm")
        eresults = sql_query2('''SELECT * FROM buildings WHERE Building_Name = ? AND Room = ?''', (ebname, erm))
    results = sql_query('''SELECT * FROM buildings''')
    return render_template("buildings.html", eresults = eresults, results = results)


@app.route("/building/edit", methods = ["POST", "GET"]) # This is used when the user submits an edited record
def sql_buildingedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        old_Building_Name = request.form["old_Building_Name"]
        old_Room = request.form["old_Room"]
        Building_ID = request.form["Building_ID"]
        Building_Name = request.form["Building_Name"]
        Section = request.form["Section"]
        Room = request.form["Room"]
        sql_edit_insert('''UPDATE buildings SET Building_ID = ?, Building_Name = ?, Section = ?, Room = ? WHERE Building_Name = ? AND Room = ?''', (Building_ID, Building_Name, Section, Room, old_Building_Name, old_Room))
    results = sql_query('''SELECT * FROM buildings''')
    msg = "/building/addbuilding"
    return render_template("building_table.html", results = results) 


# App routes for CRUD - Equipment details
@app.route("/equipment")
def sql_equipment():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM equipment''')
    msg = "equipment/addequipment"
    return render_template("equipment_table.html", results = results, msg = msg)


@app.route("/equipment/addequipment")
def addequipment():
    return render_template("equipment.html")


@app.route("/equipment/insert", methods = ["POST","GET"])   # this is used when the user inserts a new record 
def sql_equipmentinsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        Building_ID = request.form["Building_ID"]
        Equipment_Name = request.form["Equipment_Name"]
        Part = request.form["Part"]
        Make = request.form["Make"]
        Make_Date = request.form["Make_Date"]
        Catalogue_No = request.form["Catalogue_No"]
        Frame = request.form["Frame"]
        Model_No = request.form["Model_No"]
        Serial_No = request.form["Serial_No"]
        ID_No = request.form["ID_No"]
        Power_hp = request.form["Power_hp"]
        Voltage_V = request.form["Voltage_V"]
        Current_amp = request.form["Current_amp"]
        RPM = request.form["RPM"]
        Frequency_hz = request.form["Frequency_hz"]
        PH = request.form["PH"]
        HD_FT = request.form["HD_FT"]
        CAP_GPM = request.form["CAP_GPM"]
        Date_installed = request.form["Date_installed"]
        Remarks = request.form["Remarks"]
        sql_edit_insert('''INSERT INTO equipment (Building_ID, Equipment_Name, Part, Make, Make_Date, Catalogue_No, \
            Frame, Model_No, Serial_No, ID_No, Power_hp, Voltage_V, Current_amp, RPM, Frequency_hz, PH, HD_FT, CAP_GPM, \
                Date_installed, Remarks) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (Building_ID, Equipment_Name, Part, Make, Make_Date, Catalogue_No, Frame, Model_No, Serial_No, ID_No, Power_hp, Voltage_V, Current_amp, RPM, Frequency_hz, PH, HD_FT, CAP_GPM, Date_installed, Remarks)) 
    results = sql_query('''SELECT * FROM equipment''')
    return render_template("equipment_table.html", results = results)


@app.route("/equipment/deleteequipment", methods = ["POST", 'GET']) # this is used when a user deletes a record (row) from the buildings table
def sql_equipmentdelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == "GET":
        qname = request.args.get("qname")
        part = request.args.get("part")
        sql_delete('''DELETE FROM equipment WHERE Equipment_Name = ? AND Part = ?''', (qname, part))
    results = sql_query('''SELECT * FROM equipment''')
    msg = "./addequipment"
    return render_template("equipment_table.html", results = results, msg = msg)


@app.route("/equipment/query_equipmentedit", methods = ["POST", "GET"]) # This is used when the user clicks on the Edit button
def sql_equipmentqueryedit():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == "GET":
        eqname = request.args.get("eqname") # e = for editing
        epart = request.args.get("epart")
        eresults = sql_query2('''SELECT * FROM equipment WHERE Equipment_Name = ? AND Part = ?''', (eqname, epart))
    results = sql_query('''SELECT * FROM equipment''')
    return render_template("equipment.html", eresults = eresults, results = results)


@app.route("/equipment/edit", methods = ["POST", "GET"]) # This is used when the user submits an edited record
def sql_equipmentedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == "POST":
        old_Equipment_Name = request.form["old_Equipment_Name"]
        old_Part = request.form["old_Part"]
        Building_ID = request.form["Building_ID"]
        Equipment_Name = request.form["Equipment_Name"]
        Part = request.form["Part"]
        Make = request.form["Make"]
        Make_Date = request.form["Make_Date"]
        Catalogue_No = request.form["Catalogue_No"]
        Frame = request.form["Frame"]
        Model_No = request.form["Model_No"]
        Serial_No = request.form["Serial_No"]
        ID_No = request.form["ID_No"]
        Power_hp = request.form["Power_hp"]
        Voltage_V = request.form["Voltage_V"]
        Current_amp = request.form["Current_amp"]
        RPM = request.form["RPM"]
        Frequency_hz = request.form["Frequency_hz"]
        PH = request.form["PH"]
        HD_FT = request.form["HD_FT"]
        CAP_GPM = request.form["CAP_GPM"]
        Date_installed = request.form["Date_installed"]
        Remarks = request.form["Remarks"]
        sql_edit_insert('''UPDATE equipment SET Building_ID = ?, Equipment_Name = ?, Part = ?, Make = ?, Make_Date = ?, Catalogue_No = ?, Frame = ?, Model_No = ?, Serial_No = ?, ID_No = ?, Power_hp = ?, Voltage_V = ?, Current_amp = ?, RPM = ?, Frequency_hz = ?, PH = ?, HD_FT = ?, CAP_GPM = ?, Date_installed = ?, Remarks = ? WHERE Equipment_Name = ? AND Part = ?''', (Building_ID, Equipment_Name, Part, Make, Make_Date, Catalogue_No, Frame, Model_No, Serial_No, ID_No, Power_hp, Voltage_V, Current_amp, RPM, Frequency_hz, PH, HD_FT, CAP_GPM, Date_installed, Remarks, old_Equipment_Name, old_Part))
    results = sql_query('''SELECT * FROM equipment''')
    msg = "/equipment/addequipment"
    return render_template("equipment_table.html", results = results) 

if __name__ == "__main__":
    app.run(debug = True)