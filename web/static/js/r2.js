
    // var oTbl;
    // //Row 추가
    // function insRow() {
    //     oTbl = document.getElementById("regSynValue");
    //     var oRow = oTbl.insertRow();
        
    //     var oCell = oRow.insertCell();

    //     var frmTag = "<input type=text name=addText placeholder='위에서 입력한 값의 동의어를 입력하세요(예:복제하기, 똑같이 만들기...)'>";

    //     oCell.innerHTML = frmTag;
    // }
    
    function insRow(){
		var div = document.createElement('div');
		div.innerHTML = document.getElementById('regSynValue').innerHTML;
		document.getElementById('field').appendChild(div);
	}

	function remove_item(obj){
		document.getElementById('field').removeChild(obj.parentNode);
	}
