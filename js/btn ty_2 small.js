function attachAddr(){
    const str = `<li>
          제목 <input type="text" name="urlTitle" id="urlTitle" maxlength="80" />
                    주소 <input type="text" name="url" id="url" maxlength="900" />
          <a href="#delete" class="btn ty_3 small" onclick="attach.deleteEmpty(this);">삭제</a>
          </li>`;
    $("#juso24").append(str); // JQuery를 이용해서 juso24라는 id값을 가져와서 그곳에 append 시킨다.
  }