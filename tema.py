# I M P O R T S -----------------------------
import tkinter as tk
import tkinter.messagebox
from easygui import fileopenbox
import xmltodict, json
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from easygui import fileopenbox
import lxml.etree as ETX

# V I E W  ----------------------------------

root = tk.Tk() #main_frame
root.title("XIS")


T_left = tk.Text(root, height=60, width=105,  font=("Helvetica", 12), background="black", foreground="white") #left text box
T_right = tk.Text(root, height=60, width=105,  font=("Helvetica", 12), background="black", foreground="white") #right text box

json_global = '' # will contain the json generated string
xml_global = '' # will contain the xml generated string
xml_file_path = '' # will contain the path to xml file
json_file_path = '' # will contain the path to json file

def load_xml_file():
    global T_left, T_right, xml_file_path, json_global 
    
    # read the xml file path 
    xml_file_path = fileopenbox() 
    
    try:
        # extract the xml string
        tree = ET.parse(xml_file_path) 
        root = tree.getroot()
        xmlstr = ET.tostring(root, encoding='utf8', method='xml')

        # convert the xml string to json format
        json_global = json.dumps(xmltodict.parse(xmlstr), indent=4)

        # write to text boxes
        T_left.config(state=tk.NORMAL)
        T_right.config(state=tk.NORMAL)
        T_left.delete(1.0, tk.END)
        T_right.delete(1.0, tk.END)
        T_left.insert(tk.END, xmlstr.decode('utf-8'))
        T_right.insert(tk.END, json_global) 
        T_left.config(state=tk.DISABLED)
        T_right.config(state=tk.DISABLED)
    except Exception as e:
        tkinter.messagebox.showinfo("Bad file", e)
    
    
    
def load_json_file():
    global T_left, T_right, json_file_path, xml_global

    # read the json file path 
    json_file_path = fileopenbox()
    
    try:
        # read the file
        obj_r = json.loads(open(json_file_path,'r').read())

        # convert it to xml
        xml = dicttoxml(obj_r)
        dom = parseString(xml)

        # apply toprettyxml to prettify the text
        xml_global = dom.toprettyxml()

        # write to text boxes 
        T_left.config(state=tk.NORMAL)
        T_right.config(state=tk.NORMAL)
        T_left.delete(1.0, tk.END)
        T_right.delete(1.0, tk.END)
        T_left.insert(tk.END, json.dumps(obj_r, indent=4))
        T_right.insert(tk.END, xml_global)
        T_left.config(state=tk.DISABLED)
        T_right.config(state=tk.DISABLED)
    except Exception as e:
        tkinter.messagebox.showinfo("Bad file", e)
    

def get_xml(): 
    global xml_global, json_file_path
    with open(json_file_path+'_xml_conv.xml', "w") as text_file:
        text_file.write(xml_global)

def get_json():
    global json_global, xml_file_path
    with open(xml_file_path+'_json_conv.json', "w") as text_file:
        text_file.write(json_global)

def show_html_from_xml_xsl(html_str):
    html_view = tk.Tk() #html frame
    html_view.title("html")
    T_html = tk.Text(html_view, height=60, width=105,  font=("Helvetica", 12), background="black", foreground="white") #left text box
    
    T_right.config(state=tk.NORMAL)
    T_html.delete(1.0, tk.END)
    T_html.insert(tk.END, html_str)
    T_html.config(state=tk.DISABLED)
    
    T_html.pack(fill=tk.BOTH)
    T_html.mainloop() # start the main loop 

def load_xsl():
    global xml_file_path
    
    # read the xsh file path 
    xsl_path = fileopenbox()
    
    try:
        # read the xml and the xsl files
        dom = ETX.parse(xml_file_path)
        xslt = ETX.parse(xsl_path)
        
        # generate the html binary from the xml and the xsl file
        transform = ETX.XSLT(xslt)
        newdom = transform(dom)
        
        html_str = ETX.tostring(newdom, pretty_print=True).decode('utf-8') # parse it to string

        with open(xsl_path+'_html_generated.html', "w") as text_file: # save the html file
            text_file.write(html_str)
        
        show_html_from_xml_xsl(html_str) # show the output in the app
    except Exception as e:
        tkinter.messagebox.showinfo("Something goes wrong", e)
    

load_xml = tk.Button(root, text="Load xml", command=load_xml_file) # generate the button that load the xml file
load_json = tk.Button(root, text="Load json", command=load_json_file) # generate the button that load the json file
download_xml = tk.Button(root, text="Get xml", command=get_xml) # generate the button that load save the generated xml
download_json = tk.Button(root, text="Get json", command=get_json) # generate the button that load save the generated json
load_xsl = tk.Button(root, text="Load xsl", command=load_xsl) # generate the button that load the xml file


load_xml.pack(side=tk.TOP)
load_json.pack(side=tk.TOP)
download_xml.pack(side=tk.BOTTOM)
download_json.pack(side=tk.BOTTOM)

load_xsl.pack(side=tk.BOTTOM)

T_left.pack(side=tk.LEFT)
T_right.pack(side=tk.RIGHT)

root.mainloop() # start the main loop 