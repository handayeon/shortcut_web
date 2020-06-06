
    
    function insRow(){
		var div = document.createElement('div');
		div.innerHTML = document.getElementById('regSynValue').innerHTML;
		document.getElementById('field').appendChild(div);
	}

	function remove_item(obj){
		// obj.parentNode 를 이용하여 삭제
		document.getElementById('field').removeChild(obj.parentNode);
	}
