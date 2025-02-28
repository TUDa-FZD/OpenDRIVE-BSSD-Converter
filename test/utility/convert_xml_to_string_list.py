import xml.etree.ElementTree as ET

def convert_xml_to_string_list(xml_element):
    """
    This function acts as a help-function for the testing-function which need to assert the equality of two xml-elements.
    As the assertion of two xml-elements does not work due to inequal tabs, newlines and whitespaces, the xml-elements have to
    be converted to strings. To allow comparing the strings, all tabs and newlines are deleted and all characters that are 
    connected without any whitespace are added as an element to a list. This list is the basis for the assertion.

    Parameters
    ----------
    xml_element : etree.ElementTree.Element
        Element which should be converted to a list of strings.

    Returns
    -------
    xml_element_string : list
        List with single string-elements, generated from input xml-element

    """
    
    #Converting xml-element to one single string
    xml_element_string = ET.tostring(xml_element, encoding="unicode")     
    
    #Assure that all xml-elements in string are separated by a space
    xml_element_string = xml_element_string.replace("><", "> <")
    
    #Create list which contains string-elements based on whitespaces in global string
    xml_element_string = xml_element_string.split()
    
    return xml_element_string