from typing import Tuple


class State():
    def __init__(self, value, name=""):
        self.tag = "STATE"
        self.name = name
        self.value = str(value)
        if type(value) == str:
            self.type = "string"
        elif type(value) == bool:
            self.type = "boolean"
        elif type(value) == int:
            self.type = "int"
        else:
            self.type = "unknown"


class Wrapped():
    def __init__(self, *states: Tuple[State]):
        self.tag = "WRAPPED_OPTION"
        self.states = states
        self.classname = "ghidra.framework.options.Wrapped{}".format(
            self.__class__.__name__)


class Color(Wrapped):
    def __init__(self, color: str):
        super().__init__(
            State(color, "color")
        )


class Font(Wrapped):
    def __init__(self, size: int, style: int, family: str):
        super().__init__(
            State(size, "size"),
            State(style, "style"),
            State(family, "family")
        )


class KeyStroke(Wrapped):
    def __init__(self, keyCode: int, modifiers: int):
        super().__init__(
            State(keyCode, "KeyCode"),
            State(modifiers, "Modifiers")
        )


preferences = {
    "Listing Fields": {
        "Cursor Text Highlight.Highlight Color": Color(-12763891),
        "Cursor Text Highlight.Scoped Write Highlight Color": Color(-16645929),
        "Cursor Text Highlight.Scoped Read Highlight Color": Color(-2686881),
        "Selection Colors.Selection Color": Color(-5308321),
        "Cursor.Highlight Cursor Line Color": Color(-14540254),
        "References Highlight.Color": Color(-14656865)
    },
    "Decompiler": {
        "Display.Color for Keywords": Color(-1),
        "Display.Background Color": Color(-15198184),
        "Display.Color for Parameters": Color(-15081473),
        "Display.Color for Highlighting Find Matches": Color(-10516601),
        "Display.Color for Globals": Color(-1316170),
        "Display.Color for Constants": Color(-7864576),
        "Display.Color for Current Variable Highlight": Color(-12763891),
        "Display.Color Default": Color(-4473925),
        "Display.Color for Types": Color(-2237184),
        "Display.Color for Variables": Color(-15081473),
        "Display.Color for Comments": Color(-16.732201),
        "Display.Color for Function names": Color(-2237184)
    },
    "Search": {
        "Highlight Color for Current Match": Color(-10516601)
    },
    "Listing Display": {
        "Background Color": Color(-15198184),
        "Mnemonic Color": Color(-1),
        "XRef Write Color": Color(-21892),
        "Address Color": Color(-9671572),
        "Function Parameters Color": Color(-2237184),
        "Function Return Type Color": Color(-16711681),
        "Comment, Referenced Repeatable Color": Color(-20561),
        "Constant Color": Color(-7864576),
        "XRef Other Color": Color(-21892),
        "EOL Comment Color": Color(-20561),
        "Labels, Primary Color": Color(-1316170),
        "Function Tag Color": Color(-57440),
        "Bytes Color": Color(-9671572),
        "Post-Comment Color": Color(-20561),
        "Plate Comment Color": Color(-16732201),
        "Labels, Unreferenced Color": Color(-1316170),
        "Entry Point Color": Color(-16728065),
        "Pre-Comment Color": Color(-20561),
        "Mnemonic, Override Color": Color(-256),
        "External Reference, Resolved Color": Color(-65370),
        "Parameter, Dynamic Storage Color": Color(-32768),
        "Parameter, Custom Storage Color": Color(-32768),
        "Registers Color": Color(-9196115),
        "Labels, Non-primary Color": Color(-2237184),
        "XRef, Offcut Color": Color(-21892),
        "Field Name Color": Color(-1),
        "XRef Read Color": Color(-21892),
        "Separator Color": Color(-5592406),
        "Function Auto-Parameters Color": Color(-2237184),
        "Comment, Automatic Color": Color(-20561),
        "XRef Color": Color(-21892),
        "Variable Color": Color(-32768),
        "Flow Arrow, Active Color": Color(-1),
        "Labels, Local Color": Color(-1316170),
        "Function Name Color": Color(-2237184),
        "Comment, Repeatable Color": Color(-20561)
    },
    "Comments": {
        "Enter accepts comment": State(True)
    },
}
