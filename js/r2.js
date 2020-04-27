
    var oTbl;
    //Row 추가
    function insRow() {
        oTbl = document.getElementById("regSynValue");
        placeholder = "수행할 작업 대표값 입력(예: 복사하기)"
        var oRow = oTbl.insertRow();
        
        var oCell = oRow.insertCell();

        var frmTag = "<input type=text name=addText style=width:900px; height:50px;> ";
        frmTag += "<input type=button value='x' onClick='removeRow()' style='cursor:hand'>";
        oCell.innerHTML = frmTag;
    }
    //Row 삭제
    function removeRow() {
        oTbl.deleteRow(oTbl.clickedRowIndex);
    }

