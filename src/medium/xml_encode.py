"""
 XML Encoding: Since XML is very verbose, you are given a way of encoding it where each tag gets
mapped to a pre-defined integer value. The language/grammar is as follows:
Element  -->  Tag Attributes END Children END
Attribute --> Tag Value 
END --> 0 
Tag --> some predefined mapping to int
Value  --> string value
For example, the following XML might be converted into the compressed string below (assuming a
mapping of family - > 1, person - >2, firstName - > 3, lastName - > 4, state
- > 5).
<family lastName="McDowell" state="CA">
   <person firstName="Gayle">Some Message</person>
</family>
Becomes:
1 4 McDowell 5 CA e 2 3 Gayle e Some Message e e
Write code to print the encoded version of an XML element (passed in Element and Attribute
objects).

"""
import dataclasses
from typing import List, Dict, Union


@dataclasses.dataclass
class Attribute:
    name: str
    value: str


@dataclasses.dataclass
class Element:
    name: str
    attributes: List[Attribute]
    children: Union[List['Element'], str]


def encode_xml(node: Element) -> None:

    # Used to keep track of the tag number
    tag: Dict[str, int] = {'value': 1}  
    encoded: List[str] = []
    encode(node, encoded, tag)
    print(' '.join(encoded))


def encode(node: Element, encoded: List[str], 
           tag: Dict[str, int]) -> None:
    curr_tag: int = get_tag(tag)
    encoded.append(str(curr_tag))
    encode_attributes(node, encoded, tag)
    encoded.append('0')
    if type(node.children) == str:
        encoded.append(str(node.children))
    else:
        for child in node.children:
            encode(child, encoded, tag)
    encoded.append('0')


def encode_attributes(node: Element, encoded: List[str], 
                      tag: Dict[str, int]) -> None:
    for attribute in node.attributes:
        curr_tag: int = get_tag(tag)
        encoded.append(str(curr_tag))
        encoded.append(attribute.value)


def get_tag(tag: Dict[str, int]) -> int:
    curr_tag: int = tag['value']
    tag['value'] += 1
    return curr_tag

'''
<family lastName="McDowell" state="CA">
   <person firstName="Gayle">Some Message</person>
</family>
'''
element = Element(
        'family', 
        [Attribute('lastName', 'McDowell'), Attribute('state', 'CA')], 
        [
            Element('person', 
                    [Attribute('firstname', 'Gayle')], 
                    'some message')
        ]
        )
encode_xml(element)
