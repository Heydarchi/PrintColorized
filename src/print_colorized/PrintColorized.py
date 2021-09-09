
class PrintColors():
        HEADER = '\033[95m'
        NORMAL = '\033[0m'
        INFO = '\033[94m'
        SUCCESS = '\033[92m'
        OMIT = '\033[09m'
        DESC = '\033[02m'
        WARNING = '\033[93m'
        ERROR = '\033[91m'
        ENDC = '\033[00m'
        BOLD = '\033[01m'
        ITALIC = '\033[03m'
        UNDERLINE = '\033[04m'

class PrintColorized:


    @staticmethod
    def defaultParams( msg, italic=False, bold=False, undeline=False):
        beginTag=""
        endTag=PrintColors.ENDC
        if italic :
            beginTag = beginTag + PrintColors.ITALIC  
            endTag =  PrintColors.ITALIC + endTag

        if bold :
            beginTag = beginTag + PrintColors.BOLD  
            endTag =  PrintColors.BOLD  + endTag

        if undeline :
            beginTag = beginTag + PrintColors.UNDERLINE  
            endTag =  PrintColors.UNDERLINE  + endTag

        return    str(beginTag) + str(msg) + str(endTag)                                   



def printNormal( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(str(msg), italic, bold, underline)
    print(PrintColors.NORMAL + msg )

def printInfo( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.INFO + msg )

def printSuccess( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.SUCCESS + msg )

def printWarning( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.WARNING + msg )

def printError( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.ERROR + msg )

def printDesc( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.DESC + msg )     

def printOmit( msg, italic=False, bold=False, underline=False):
    msg=PrintColorized.defaultParams(msg, italic, bold, underline)
    print(PrintColors.OMIT + msg ) 

def helpPrintColorized() :
    print("            Help  ")
    print("............................\n")
    printNormal("Normal")
    printSuccess("SUCCESS")
    printWarning("Warning")
    printError("Error")
    printDesc("Description")
    printInfo("Info")
    printOmit("Omit")
    print("\n......... Params  ..........\n")
    printNormal("Normal Italic", italic=True)
    printNormal("Normal Bold", bold=True)
    printNormal("Normal Underline", underline=True)
    print("\n............................")      

if __name__ == '__main__':
    helpPrintColorized()


