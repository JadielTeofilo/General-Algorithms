"""
XML Encoding: Since XML is very verbose, you are given a way of encoding it where each tag gets
mapped to a pre-defined integer value. The language/grammar is as follows :
Element --) Tag Attributes END Chil dren END
Attribute --) Tag Value
END -- ) e
Tag -- ) some predefined mapping to int
Value -- ) string value
For example, the following XML might be converted into the compressed string below (assuming a
mapping of family - > 1, person - >2, firstName - > 3, lastName - > 4, state
->
 5) .
<family lastName="McDowell" state="CA">
<person firstName="Gayle")Some Message </person>
</family>
Becomes:
1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
Write code to print the encoded version of an XML element (passed in Element and Attribute
objects).

class Element:
	attributes: List[Attribute]
	value: Union[str, Element]

In - root: Element

"""
import dataclasses
from typing import List, Optional, Union


@dataclasses.dataclass
class Attribute:
	
	value: str


@dataclasses.dataclass
class Element:
	name: str
	attributes: List[Attribute]
	children: Union[None, str, List['Element']]


def xml_encode(root: Element) -> str:
	elements: List[str] = []
	encode(root, tag=1, elements)
	return ''.join(elements)


def encode(root: Element, tag: int, 
		   elements: List[Element]) -> None:
	
