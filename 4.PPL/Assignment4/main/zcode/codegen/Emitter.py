from Utils import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from CodeGenError import *


class Zcode(Type):
    pass

class VarZcode(Zcode):
    def __str__(self):
        return f"VarZcode(type={self.typ},name={self.name},index={self.index},line={self.line},init={self.init})"
    
    def __init__(self, name, typ, index, init = False):
        self.name = name
        self.typ = typ
        self.init = init
        self.line = 0 
        self.index = index 

class FuncZcode(Zcode):
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},name={self.name},line={self.line})"
    
    def __init__(self, name, typ, param):
        self.name = name
        self.typ = typ
        self.line = 0
        self.param = param

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list() 
        self.jvm = JasminCode() 

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is BoolType: 
            return "Z"
        elif typeIn is VoidType: 
            return "V"
        elif typeIn is VarZcode: 
            return "None"
        elif typeIn is Zcode: 
            return "LZCodeClass;"
        elif typeIn is FuncZcode: 
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.param))) + ")" + self.getJVMType(inType.typ) if inType.typ else "None"
        elif typeIn is StringType: 
            return "Ljava/lang/String;"
        elif typeIn is NumberType: 
            return "F"
        elif typeIn is ArrayType:
            return "[" * len(inType.size)  + self.getJVMType(inType.eleType)
        return "Ljava/lang/Object;"
    
    def emitNEWARRAY(self, in_, frame):
        val = ""
        if type(in_) is BoolType:
            val = "boolean"
        elif type(in_) is StringType:
            return self.emitANEWARRAY(in_, frame)
        elif type(in_) is NumberType:
            val = "float"
        return self.jvm.emitNEWARRAY(val)
    
    def emitPUSHCONST(self, in_, typ, frame):
        frame.push()
        if type(typ) is NumberType:
            f = float(in_)
            rst = "{0:.4f}".format(f)
            if rst == "0.0" or rst == "1.0" or rst == "2.0":
                return self.jvm.emitFCONST(rst)
            return self.jvm.emitLDC(rst)
        elif type(typ) is BoolType:
            if in_:
                return self.jvm.emitICONST(1)
            return self.jvm.emitICONST(0)    
        elif type(typ) is StringType:
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)
        
    def emitALOAD(self, in_, frame):
        frame.pop()
        if type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is NumberType:
            return self.jvm.emitFALOAD()
        else:
            raise IllegalOperandException(str(in_))  
        
    def emitF2I(self, frame):
        return "\tf2i\n"
        
    def emitASTORE(self, in_, frame):
        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif  type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))
        
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        get = self.getJVMType(inType)
        return self.jvm.emitVAR(in_, varName, get, fromLabel, toLabel)
    
    def emitREADVAR(self, name, inType, index, frame):
        frame.push()
        if name == "this":
            return self.jvm.emitALOAD(index)
        elif type(inType) is NumberType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        elif type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)
        
    def emitWRITEVAR(self, name, inType, index, frame):
        frame.pop()
        if type(inType) is NumberType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        else:
            raise IllegalOperandException(name) 
        
    def emitATTRIBUTE(self, lexeme, in_, isFinal = False, value = None):
        get = self.getJVMType(in_)
        return self.jvm.emitSTATICFIELD(lexeme, get, isFinal)

    def emitGETSTATIC(self, lexeme, in_, frame):
        get = self.getJVMType(in_)
        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, get)

    def emitPUTSTATIC(self, lexeme, in_, frame):
        get = self.getJVMType(in_)
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, get)
    
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        typ = in_
        param = typ.param
        list(map(lambda x: frame.pop(), param))
        if not type(typ.typ) is VoidType:
            frame.push()
        get = self.getJVMType(in_)
        return self.jvm.emitINVOKESTATIC(lexeme, get)
    
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_= None):
        cond1 = not lexeme is None
        cond2 = not in_ is None
        if cond1 and cond2:
            typ = in_
            param = typ.param
            list(map(lambda x: frame.pop(), param))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            get = self.getJVMType(in_)
            return self.jvm.emitINVOKESPECIAL(lexeme, get)
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        typ = in_
        param = typ.param
        list(map(lambda x: frame.pop(), param))
        if type(typ) is VoidType:
            frame.pop()
        get = self.getJVMType(in_)
        return self.jvm.emitINVOKEVIRTUAL(lexeme, get)
    
    def emitNEGOP(self, in_, frame):
        return self.jvm.emitFNEG()
    
    def emitANEWARRAY(self, in_, frame):
        val = ""
        if type(in_) is NumberType:
            val = "float"
        elif type(in_) is StringType:
            val = "java/lang/String"
        elif type(in_) is ArrayType:
            val = self.getJVMType(in_)
        elif type(in_) is BoolType:
            val = "boolean"
        return self.jvm.emitANEWARRAY(val)

    def emitNOT(self, in_, frame):
        labelFirst = frame.getNewLabel()
        labelSecond = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(labelFirst, frame))
        result.append(self.emitPUSHCONST(True, in_, frame))
        result.append(self.emitGOTO(labelSecond, frame))
        result.append(self.emitLABEL(labelFirst, frame))
        result.append(self.emitPUSHCONST(False, in_, frame))
        result.append(self.emitLABEL(labelSecond, frame))
        return ''.join(result)

    def emitADDOP(self, lexeme, in_, frame):
        frame.pop()
        if lexeme == "+":
            return self.jvm.emitFADD()
        return self.jvm.emitFSUB()

    def emitMULOP(self, lexeme, in_, frame):
        frame.pop()
        if lexeme == "*":
            return self.jvm.emitFMUL()
        return self.jvm.emitFDIV()



    def emitANDOP(self, frame):
        frame.pop()
        return self.jvm.emitIAND()
    
    def emitOROP(self, frame):
        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        result = list()
        labelFs = frame.getNewLabel()
        labelOs = frame.getNewLabel()

        frame.pop()
        frame.pop()
        result.append(self.jvm.emitFCMPL())
        if op == ">":
            result.append(self.jvm.emitIFLE(labelFs))
        elif op == "=":
            result.append(self.jvm.emitIFEQ(labelFs))   
            result.append(self.emitPUSHCONST(False, BoolType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelOs, frame))
            result.append(self.emitLABEL(labelFs, frame))
            result.append(self.emitPUSHCONST(True, BoolType(), frame))
            result.append(self.emitLABEL(labelOs, frame)) 
            return ''.join(result)
        elif op == "<=":
            result.append(self.jvm.emitIFGT(labelFs))
        elif op == "!=":
            result.append(self.jvm.emitIFEQ(labelFs)) 
        elif op == ">=":
            result.append(self.jvm.emitIFLT(labelFs))
        elif op == "<":
            result.append(self.jvm.emitIFGE(labelFs))
  
        result.append(self.emitPUSHCONST(True, BoolType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelOs, frame))
        result.append(self.emitLABEL(labelFs, frame))
        result.append(self.emitPUSHCONST(False, BoolType(), frame))
        result.append(self.emitLABEL(labelOs, frame))
        return ''.join(result)

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        get = self.getJVMType(in_)
        return self.jvm.emitMETHOD(lexeme, get, isStatic)

    def emitENDMETHOD(self, frame):
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def emitIFTRUE(self, label, frame):
        frame.pop()
        return self.jvm.emitIFGT(label)

    def emitIFFALSE(self, label, frame):
        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitDUP(self, frame):
        frame.push()
        return self.jvm.emitDUP()

    def emitI2F(self, frame):
        return self.jvm.emitI2F()

    def emitRETURN(self, in_, frame):
        if type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        elif type(in_) is StringType or type(in_) is ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is NumberType:
            frame.pop()
            return self.jvm.emitFRETURN()

    def emitLABEL(self, label, frame):
        return self.jvm.emitLABEL(label)
    
    def emitGOTO(self, label, frame):
        return self.jvm.emitGOTO(str(label))

    def emitPROLOG(self, name, parent):
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        return self.jvm.emitLIMITLOCAL(num)
    
    def emitMULTIANEWARRAY(self, in_, frame):
        if type(in_) is ArrayType:
            dimensions = len(in_.size)
            get = self.getJVMType(in_)
            return self.jvm.emitMULTIANEWARRAY(get, str(dimensions))

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    def printout(self, in_):
        self.buff.append(in_)
    
    def clearBuff(self):
        self.buff.clear()

    def printIndexNew(self):
        return len(self.buff) - 1
    
    def setType(self, in_):
        if type(in_) is VarZcode: 
            typ = self.getJVMType(in_.typ)
        else: 
            typ = self.getJVMType(in_)
        self.buff[in_.line] = self.buff[in_.line].replace("None", typ)
      
    def updateType(self, index, type):
        pass