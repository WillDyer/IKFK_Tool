import maya.cmds as cmds
import maya.api.OpenMaya as om
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

#CHANGE LOCATION IF UI FILE NOT LOADING
UI_FILE = "E:\YR2\Maya\RIGGIN_SCRIPTS\main_window.ui"

ui_file = QFile(UI_FILE)
ui_file.open(QFile.ReadOnly)
loader = QUiLoader()
ui = loader.load(ui_file)
ui_file.close()

#TextBox Setup
#CheckBoxs Setup

def loadInitialValues():  
    updateCheckbox()
    onChanged()
    updateComboBox()

def updateCheckbox():
    layersValue = ui.createLayers_CheckBox.isChecked() 
    layersValue = str(layersValue)
    global createLayers
    createLayers = layersValue
    global controlsValue
    controlsValue = ui.createControlsCheckBox.isChecked()
    controlsValue = str(controlsValue)        
    global IkHandleValue
    IkHandleValue = ui.createIkHandle_checkBox.isChecked()
    IkHandleValue = str(IkHandleValue)
    if IkHandleValue == "False":
        ui.createPollVector_CheckBox.setVisible(False)
        ui.createPollVector_CheckBox.setChecked(False)
    else:
        ui.createPollVector_CheckBox.setVisible(True) 
    global PollVectorValue
    PollVectorValue = ui.createPollVector_CheckBox.isChecked()
    PollVectorValue = str(PollVectorValue)        
    constrainJointsValue = ui.constrainJoints_CheckBox.isChecked()
    constrainJointsValue = str(constrainJointsValue)        
    parentIkValue = ui.parentIk_CheckBox.isChecked()
    parentIkValue = str(parentIkValue)
    global parentIk
    parentIk = parentIkValue      
    parentFkValue = ui.parentFk_CheckBox.isChecked()
    parentFkValue = str(parentFkValue)
    global parentFk
    parentFk = parentFkValue      
    if constrainJointsValue == "False":
        ui.parentFk_CheckBox.setVisible(False)
        ui.parentFk_CheckBox.setChecked(False)
        ui.parentIk_CheckBox.setVisible(False)
        ui.parentIk_CheckBox.setChecked(False)
    else:
        ui.parentFk_CheckBox.setVisible(True)
        ui.parentIk_CheckBox.setVisible(True)
    global rigToIkFkValue
    rigToIkFkValue = ui.rigToIkFk_CheckBox.isChecked()
    rigToIkFkValue = str(rigToIkFkValue)        
    if rigToIkFkValue == "False":
        ui.createIkFkSwitch_CheckBox.setVisible(False)
        ui.createIkFkSwitch_CheckBox.setChecked(False)
    else:
        ui.createIkFkSwitch_CheckBox.setVisible(True)
    global createIkFkSwitchValue
    createIkFkSwitchValue = ui.createIkFkSwitch_CheckBox.isChecked()
    createIkFkSwitchValue = str(createIkFkSwitchValue)        
    createCustomAttrValue = ui.createCustomAttr_CheckBox.isChecked()
    createCustomAttrValue = str(createCustomAttrValue)        
    createReverseFootValue = ui.createReverseFoot_CheckBox.isChecked()
    createReverseFootValue = str(createReverseFootValue)        
    clavicleIkValue = ui.clavicleIk_CheckBox.isChecked()
    clavicleIkValue = str(clavicleIkValue)        
    
def onChanged():
    amountOfJointsValue = ui.amountOfJointsText.text()
    amountOfJointsValue = int(amountOfJointsValue)
    global amount
    amount = amountOfJointsValue

    print(amountOfJointsValue)
    controlSizeValue = ui.controlSize_text.text()
    controlSizeValue = int(controlSizeValue)
    global controlRadius
    controlRadius = controlSizeValue
    
def updateComboBox():
    leftOrRightValue = ui.leftOrRightDropDown.currentText()
    leftOrRightValue = str(leftOrRightValue)
    global leftOrRight
    leftOrRight = leftOrRightValue
    bodyAreaValue = ui.bodyAreaDropDown.currentText()
    bodyAreaValue = str(bodyAreaValue)
    global bodyArea
    bodyArea = bodyAreaValue
    print(bodyAreaValue)
    bodyTypeValue = ui.bodyTypeDropDown.currentText()
    bodyTypeValue = str(bodyTypeValue)
    global bodytype
    bodytype = bodyTypeValue
    comboBoxValue = ui.comboBox.currentText()
    comboBoxValue = str(comboBoxValue)
    global constraintOrOPM
    constraintOrOPM = comboBoxValue

def resetPressed():
    print("RESET")
def closePressed():
    ui.close()

#What happens when you click a button
ui.ResetButton.clicked.connect(resetPressed)
ui.CloseButton.clicked.connect(closePressed)

    
ui.leftOrRightDropDown.currentIndexChanged.connect(updateComboBox)
ui.bodyAreaDropDown.currentIndexChanged.connect(updateComboBox)
ui.bodyTypeDropDown.currentIndexChanged.connect(updateComboBox)
ui.comboBox.currentIndexChanged.connect(updateComboBox)

ui.amountOfJointsText.textEdited.connect(onChanged)
ui.controlSize_text.textEdited.connect(onChanged)

ui.createLayers_CheckBox.stateChanged.connect(updateCheckbox)
ui.createControlsCheckBox.stateChanged.connect(updateCheckbox)
ui.createIkHandle_checkBox.stateChanged.connect(updateCheckbox)
ui.createPollVector_CheckBox.stateChanged.connect(updateCheckbox)
ui.constrainJoints_CheckBox.stateChanged.connect(updateCheckbox)
ui.parentIk_CheckBox.stateChanged.connect(updateCheckbox)
ui.parentFk_CheckBox.stateChanged.connect(updateCheckbox)
ui.rigToIkFk_CheckBox.stateChanged.connect(updateCheckbox)
ui.createIkFkSwitch_CheckBox.stateChanged.connect(updateCheckbox)
ui.createCustomAttr_CheckBox.stateChanged.connect(updateCheckbox)
ui.createReverseFoot_CheckBox.stateChanged.connect(updateCheckbox)
ui.clavicleIk_CheckBox.stateChanged.connect(updateCheckbox) 

#VariablesNeededCreation
jointsList = []
rigJointsList = []
ikJointsList = []
fkJointsList = []
ikParentList = []
fkParentList = []
jointsSplitList = []
solverType = ["ikRPsolver", "ikSCsolver", "ikSplineSolver"]
fkCtrlList = []
ikCtrlList = []
grpCtrlList = []
ikgrpCtrlList = []
ikHandle_name = ""
ikgroupSelect = []
ikHandleList = []
ikControlNameList = []
nameList = []
append_firstList = []
append_secondList = []
append_thirdList = []
ikfkConstraints = []
global pvCreated
pvCreated = False

topJoint = cmds.ls(sl=True, typ='joint')

def offsetParentMatrix():
#This script bakes Transform of node(eg: Nurbscurve_Ctrl) to its Offset Parent Matrix which then acts as its rest matrix. Credit to Muream @gitHubGist 

    TRANSFORM_NODETYPES = ["transform", "joint"]

    def has_non_default_locked_attributes(node):
        locked_attributes = []
        for attribute in ["translate", "rotate", "scale", "jointOrient"]:
            default_value = 1 if attribute == "scale" else 0
            for axis in "XYZ":
                if cmds.attributeQuery(attribute + axis, node=node, exists=True):
                    attribute_name = "{}.{}{}".format(node, attribute, axis)
                    current_value = cmds.getAttr(attribute_name)
                    if cmds.getAttr(attribute_name, lock=True) and current_value != default_value:
                        return True

    def reset_transforms(node):
        for attribute in ["translate", "rotate", "scale", "jointOrient"]:
            value = 1 if attribute == "scale" else 0
            for axis in "XYZ":
                if cmds.attributeQuery(attribute + axis, node=node, exists=True):
                    attribute_name = "{}.{}{}".format(node, attribute, axis)
                    if not cmds.getAttr(attribute_name, lock=True):
                        cmds.setAttr(attribute_name, value)

    def bake_transform_to_offset_parent_matrix(node):
        if cmds.nodeType(node) not in TRANSFORM_NODETYPES:
            raise ValueError("Node {} is not a transform node".format(node))

        if has_non_default_locked_attributes(node):
            raise RuntimeError("Node {} has at least one non default locked attribute(s)".format(node))

        local_matrix = om.MMatrix(cmds.xform(node, q=True, m=True, ws=False))
        offset_parent_matrix = om.MMatrix(cmds.getAttr(node + ".offsetParentMatrix"))
        baked_matrix = local_matrix * offset_parent_matrix
        cmds.setAttr(node + ".offsetParentMatrix", baked_matrix, type="matrix")

        reset_transforms(node)

    def bake_transform_to_offset_parent_matrix_selection():
        for node in cmds.ls(sl=True):
            bake_transform_to_offset_parent_matrix(node)

    if __name__ == "__main__":
        bake_transform_to_offset_parent_matrix_selection()


def duplicateIkFkJoints():
    jointsList = cmds.listRelatives(topJoint,ad=True, typ='joint')
    jointsList.append(topJoint[0])
    jointsList.reverse()
    global toBeDuplicated
    toBeDuplicated = jointsList[:amount]
    
    for item in jointsList:

        if item in toBeDuplicated:
            cmds.select(item, r=True)
            cmds.joint()
            cmds.parent(w=True)
            newJoint = cmds.ls(sl=True, typ='joint')
            ikJointsList.append(newJoint[0])

            cmds.select(item, r=True)
            cmds.joint()
            cmds.parent(w=True)
            newJoint = cmds.ls(sl=True, typ='joint')
            fkJointsList.append(newJoint[0])
        else:
            #print(item, "is not in list")
            pass
            
def jointsRename():
    #gets joints selected based off the amountOfJoints via ui
    for x in range(len(toBeDuplicated)):
        nameTempList = toBeDuplicated[x].split("_")[2]
        nameList.append(nameTempList)
    
    for i in range(amount):
        cmds.rename(ikJointsList[i], 'jnt_ik_' + nameList[i] + "_" + leftOrRight)
        ikJointsList[i] = 'jnt_ik_' + nameList[i] + "_" + leftOrRight
        cmds.rename(fkJointsList[i], 'jnt_fk_' + nameList[i] + "_" + leftOrRight)
        fkJointsList[i] = 'jnt_fk_' + nameList[i] + "_" + leftOrRight

def parentJoints():
    for i in range(amount):
        cmds.select(fkJointsList[i], r=True)
        offsetParentMatrix()
    
    ikJointsList.reverse()
    fkJointsList.reverse()

    #Optional Layer Creation
    if createLayers == "True":
        ikLayer = cmds.createDisplayLayer(ikJointsList, name="IK")
        cmds.setAttr("{}.overrideRGBColors".format(ikLayer), True)
        cmds.setAttr("{}.overrideColorRGB".format(ikLayer), 0.169, 0.334, 1)
        fkLayer = cmds.createDisplayLayer(fkJointsList, name="FK")
        cmds.setAttr("{}.overrideRGBColors".format(fkLayer), True)
        cmds.setAttr("{}.overrideColorRGB".format(fkLayer), 1, 0.183, 0.233)
    else:
        pass
    
    amountParent = amount - 1
    
    if parentIk == "True":
        for i in range(amountParent):
            cmds.parent(ikJointsList[i],ikJointsList[i+1])
    if parentFk == "True":
        for i in range(amountParent):
            cmds.parent(fkJointsList[i],fkJointsList[i+1])
    

def createIkHandle():
    
    for i in range(len(ikJointsList)):
        temp = ikJointsList[i].split("_")[2]
        jointsSplitList.append(temp)
    
    #check joints for correct joints to create apon
    if "shoulder" in jointsSplitList:
        firstJoint = cmds.ls("jnt_ik_shoulder_"+leftOrRight,typ="joint")
    elif "hip" in jointsSplitList:
        firstJoint = cmds.ls(f"jnt_ik_hip_"+leftOrRight,typ="joint")
    if "wrist" in jointsSplitList:
        endJoint = cmds.ls("jnt_ik_wrist_"+leftOrRight,typ="joint")
    elif "ankle" in jointsSplitList:
        endJoint = cmds.ls("jnt_ik_ankle_"+leftOrRight,typ="joint")
    else:
        print("No joints meet IK naming requirements")
    
    #from above create IKHandle
    global ikHandle_name
    if bodytype == "bipedal_arm":
        cmds.ikHandle(n="ikHandle_arm_"+leftOrRight, solver=solverType[0], sj=firstJoint[0], ee=endJoint[0])
        ikHandle_name = "ikHandle_arm_"+leftOrRight
        ikHandleList.append(ikHandle_name)
    elif bodytype == "bipedal_leg":
        cmds.ikHandle(n="ikHandle_leg_"+leftOrRight, solver=solverType[0], sj=firstJoint[0], ee=endJoint[0])
        ikHandle_name = "ikHandle_leg_"+leftOrRight
        ikHandleList.append(ikHandle_name)
    elif bodytype == "quadruped_arm":
        cmds.error("Waiting to be taught this")
    elif bodytype == "quadruped_leg":
        cmds.error("Waiting to be taught this")
    else:
        print("createIkHandle: No IK Handle found")

def createPV():
    #may need to change the location later
    cmds.file("E:/YR2/Maya/RIGGIN_SCRIPTS/poleVector_crv.ma", i=True)
    pvCrvShape = cmds.ls("poleVector_crv")
    global pvCrv
    pvCrv = cmds.rename(pvCrvShape, "ctrl_poleVector_"+leftOrRight)
    if "elbow" in jointsSplitList:
        pvSource = "jnt_ik_elbow_"+leftOrRight
    elif "radial" in jointsSplitList:
        pvSource = "jnt_ik_radial_"+leftOrRight
    elif "knee" in jointsSplitList:
        pvSource = "jnt_ik_knee_"+leftOrRight
    else:
        cmds.warning("No match for polevector source")
    
    cmds.matchTransform(pvCrv, pvSource,px=True,py=True,pz=True)
    if bodyArea == "arm":
        cmds.move(0,0,-50,pvCrv,r=True)
    elif bodyArea == "leg":
        cmds.move(0,0,50,pvCrv,r=True)
    cmds.poleVectorConstraint(pvCrv, ikHandle_name, n="cnst_"+pvCrv)
    cmds.setAttr(pvCrv+".rotateX",l=False,k=False)
    cmds.setAttr(pvCrv+".rotateY",l=False,k=False)
    cmds.setAttr(pvCrv+".rotateZ",l=False,k=False)
    cmds.select(pvCrv)
    offsetParentMatrix()
    
        
def createControls():
    
    for i in range(len(fkJointsList)):
        fkName = fkJointsList[i].split("_")[2]
        
        fkControlName = "ctrl_fk_"+fkName+"_"+leftOrRight
        controlShape = cmds.circle(n=fkControlName,r=controlRadius,nr=(1,0,0))
        fkCtrlList.append(controlShape[0])
        jointSelect = cmds.ls(fkJointsList[i])
        cmds.matchTransform(controlShape, jointSelect)
        
        if leftOrRight == "l":
            cmds.setAttr(fkControlName+".overrideEnabled", 1)
            cmds.setAttr(fkControlName+".overrideColor", 6)
        elif leftOrRight == "r":
            cmds.setAttr(fkControlName+".overrideEnabled", 1)
            cmds.setAttr(fkControlName+".overrideColor", 13)
        else:
            pass
    try:
        for i in range(amount):
            parents = cmds.parent(fkCtrlList[i], fkCtrlList[i+1])
    except IndexError:
        pass    
    
    #presuming wrist or ik handle joint is the first in list as list is reversed
    ikName = ikJointsList[0].split("_")[2]
    ikControlName = "ctrl_ik_"+ikName+"_"+leftOrRight
    ikControlNameList.append(ikControlName)
    ikControlShape = cmds.circle(n=ikControlName,r=controlRadius + 2,nr=(1,0,0))
    ikCtrlList.append(ikControlShape[0])
    ikGroupName = "grp_ik_"+ikName+"_"+leftOrRight
    ikGroupSelect = cmds.group(n=ikGroupName,w=1)
    ikgrpCtrlList.append(ikGroupSelect)
    ikJointSelect = cmds.ls(ikJointsList[0])
    ikResetTransforms = cmds.ls(ikControlShape)
    cmds.setAttr(ikResetTransforms[0]+".translate",0,0,0,type="double3")
    cmds.setAttr(ikResetTransforms[0]+".rotate",0,0,0,type="double3")   
    cmds.matchTransform(ikGroupName, ikJointsList[0])
    if leftOrRight == "l":
        cmds.setAttr(ikControlName+".overrideEnabled", 1)
        cmds.setAttr(ikControlName+".overrideColor", 6)
    if leftOrRight == "r":
        cmds.setAttr(ikControlName+".overrideEnabled", 1)
        cmds.setAttr(ikControlName+".overrideColor", 13)
    else:
            pass

def runOPM():
    cmds.select(ikJointsList,r=True)
    offsetParentMatrix()   
    cmds.select(fkJointsList,r=True)
    offsetParentMatrix()
    for i in range(amount):
        cmds.select(fkCtrlList[i])
        offsetParentMatrix()
        
def constraints():
    # 0 = use constraint, 1 = use OPM, set anthing above to ignore
    #parentIkFk 1 = parent, 0 = no parent
    if constraintOrOPM == "Constraints":
        if parentFk == "True":
            for i in range(len(fkJointsList)):
                tempFkJoint = fkJointsList[i].split("jnt")[1]
                ctrlSelect = "ctrl" + tempFkJoint
                cmds.parentConstraint(ctrlSelect, fkJointsList[i], mo=True)           
        else:
            pass
                    
    if constraintOrOPM == "OPM":
        if parentFk == "True":
            for i in range(len(fkJointsList)):
                tempFkJoint = fkJointsList[i].split("jnt")[1]
                ctrlSelect = "ctrl" + tempFkJoint
        
                cmds.connectAttr(ctrlSelect + '.translate', fkJointsList[i] + '.translate' )
                cmds.connectAttr(ctrlSelect + '.rotate', fkJointsList[i] + '.rotate' )
                cmds.connectAttr(ctrlSelect + '.scale', fkJointsList[i] + '.scale' )
        else:
            pass         
    else:
        pass
    
    #parent IkHandle
    try:
        cmds.parentConstraint(ikControlNameList[0], ikHandleList[0], mo=True, n="cnst_"+ikHandleList[0])
    except IndexError:
        pass
          
def rigToIkFk():
    toBeDuplicated.reverse()
    #splits lists to be able to compare names
    for x in range(len(toBeDuplicated)):
            try:
                check_firstList = toBeDuplicated[x].split("_")[2]
                append_firstList.append(check_firstList)
                check_secondList = ikJointsList[x].split("_")[2]
                append_secondList.append(check_secondList)
                check_thirdList = fkJointsList[x].split("_")[2]
                append_thirdList.append(check_thirdList)
            except IndexError:
                print("finished list")
    
    for x in range(len(toBeDuplicated)):
        try:
            if append_firstList[x] == append_secondList[x]:
                if append_firstList[x] == append_thirdList[x]:
                    constraint = cmds.parentConstraint(fkJointsList[x],ikJointsList[x], toBeDuplicated[x], mo=True,n="cnst_"+toBeDuplicated[x])
                    ikfkConstraints.append(constraint[0])
        except IndexError:
            print("No match") 

def createIkFkSwitch():
    ctrls = []
    for x in range(amount):
        try:
            ctrls.append(fkCtrlList[x])
            ctrls.append(ikCtrlList[x])
        except IndexError:
            pass
    
    ### Sets naming for the switch ###
    IKFK = ".IKFK_Switch"
    proxyAttrDisplayName = "IK/FK Switch"
    proxyAttrLongName = "IKFK_Switch"
    sourceAttr = ctrls[0]+IKFK
    
    cmds.addAttr(ctrls[0],nn=proxyAttrDisplayName,sn=proxyAttrLongName,k=True,min=0,max=1)
    cmds.addAttr(ctrls[1:],nn=proxyAttrDisplayName,sn=proxyAttrLongName,proxy=sourceAttr)
    
    ctrlsSplitTemp = []
    ctrlsSplit = []
    ctrlsSplitTemp2 = []
    ctrlsSplitName = []
    cnstNameSplit = []
    for x in range(len(ctrls)):
        ctrlsSplitTemp = ctrls[x].split("_")[1]
        ctrlsSplitTemp2 = ctrls[x].split("_")[2]
        ctrlsSplit.append(ctrlsSplitTemp)
        ctrlsSplitName.append(ctrlsSplitTemp2)

    for i in range(amount):
        print(ikfkConstraints[i])
        cnstNameSplitTemp = ikfkConstraints[i].split("_")[3]
        cnstNameSplit.append(cnstNameSplitTemp)

    reverseNode = cmds.createNode('reverse', n='IKFK_Reverse')
    cmds.connectAttr(sourceAttr,reverseNode+'.inputX')
    
    if PollVectorValue == "True":
        cmds.connectAttr(reverseNode+".outputX",pvCrv+".visibility")
    else:
        pass
    
    for i in range(len(ctrls)):
        if ctrlsSplit[i] == "ik":
            print("ikfound")
            for x in range(len(ctrls)):
                try:
                    if ctrlsSplit[x] == "ik":
                        cmds.connectAttr(reverseNode+".outputX",ctrls[x]+".visibility")
                    
                    shrtCtrl = ctrls[x]
                    cmds.connectAttr(reverseNode+".outputX",ikfkConstraints[cnstNameSplit.index(ctrlsSplitName[x])]+".jnt_ik_"+shrtCtrl[8:]+"W1")
                    if ctrlsSplit[x] == "fk":
                        cmds.connectAttr(sourceAttr,ctrls[x]+".visibility")
                    shrtCtrl = ctrls[x]
                    cmds.connectAttr(ctrls[x]+IKFK,ikfkConstraints[cnstNameSplit.index(ctrlsSplitName[x])]+".jnt_fk_"+shrtCtrl[8:]+"W0")
                except RuntimeError:
                    print("runtime error destination not found")

### CALL ON FUNCTIONSS ###  

def applyPressed():
    print("APPLY")
    if not topJoint:
        print("ERROR: Select Joints")
    
    else:
        print("Selection Found")
        duplicateIkFkJoints()
        print("Complete: Joints Duplicate")
        jointsRename()
        print("Complete: Joints Renamed")
        parentJoints()
        print("Complete: Joints Parented")
        if IkHandleValue == "True":
            createIkHandle()
            print("Complete: IK Handle")
        if PollVectorValue == "True":
            createPV()
        if controlsValue == "True":
            createControls()
            runOPM()
            constraints()
        if rigToIkFkValue == "True":
            rigToIkFk()
            print("Complet: rigToIkFkValue")
        if createIkFkSwitchValue == "True":
            createIkFkSwitch()
            print("Complete: IkFkSwitch")
            
ui.ApplyButton.clicked.connect(applyPressed)

loadInitialValues()
ui.show() 