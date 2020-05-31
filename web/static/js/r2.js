
    var oTbl;
    //Row 추가
    function insRow() {
        oTbl = document.getElementById("regSynValue");
        // placeholder = "위에서 입력한 값의 동의어를 입력하세요(예:복제하기, 똑같이 만들기...)"
        var oRow = oTbl.insertRow();
        
        var oCell = oRow.insertCell();

        var frmTag = "<input type=text name=addText style=width:900px; height:50px placeholder='위에서 입력한 값의 동의어를 입력하세요(예:복제하기, 똑같이 만들기...)'>";

        oCell.innerHTML = frmTag;
    }
   
    //Row 삭제
    function removeRow() {
        oTbl.deleteRow(oTbl.clickedRowIndex);
    }
