*** Settings ***
Library    os
Resource    ${EXEC_DIR}/Res/attach_keyword.robot
Variables    ${EXEC_DIR}/VariableFiles/config_file.py
Library    ${EXEC_DIR}/Lib/attach.py


*** Test Cases ***

TC_1.2

    Unlock A Window Folder
    Moving Source Files To Destination Folder
    Rach Request Validation
    Rach Response Validation

TC_1.30
    Moving Gnb And Dut
    Validating Gnb
    Validating Dut
TC_1.12
    Moving Files
    Reset Message
    Validating


TC_1.23
    Moving Cell And Ue
    Validating Selection Criteria
    Validating Reselection Criteria
    Finding Best Cell
    #lock a window folder
TC_1.120
    Moving Handover
    Handover Val
    Handover Verify
TC_1.121
    Moving Gnb
    Multi Gnb
    Gnb Verify
TC_1.123
    Moving Mul
    Multiuser Val
    Verifying Mul
TC_1.124
    Moving Multiple Users
    Validating Multiuser
    Verifying Multiuser


