// form tools
room_mem = null;
lang_mem = null;

// Returns the val from a form using its name if it exists, else return null
function getValFromFormName(name) {
  var e = document.getElementsByName(name)[0];
  if (e) {
    return e.value;
  }else {
    return null;
  }
}

// get the value from the room for if it exists (or if the value has existed), else return null
function getValFromRoomForm () {
  res = getValFromFormName("room");
  if (!res) {
    res = room_mem;
  } else {
    room_mem = res ;
  }
  return res;
}

// get the value from the lang form if it exists (or if the value has existed), else return null
function getValFromLangForm () {
  res =  getValFromFormName("lang");
  if (!res) {
    res = lang_mem;
  } else {
    lang_mem = res ;
  }
  return res;
}
