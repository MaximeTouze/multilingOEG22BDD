const SENTENCE_SEPARATOR = "___________________";

const GenerateImg = function (path, alt, style="", onclick=null, id=null) {
  let img = "<img style='" + style + "' src=\"" + path + "\" alt='" + alt

  if (id) {
    img += "' id='" + id;
  }
  if (onclick) {
    img += "' onclick='" + onclick;
  }
  return img + "'>";
}

const GenerateExposedImg = function (name, style="weight:100%; height:100%", onclick=null, id=null) {
  return GenerateImg("../static/exposed/" + name, name, style=style, onclick=onclick, id);
}


const ChangeSentenceDislikeButtonToLike = function (nb_sentence) {
  const onclickFunction = 'LikeSentence(' + nb_sentence + ');';
  document.getElementById('like_'+nb_sentence).classList.remove('liked');
  document.getElementById(getSentenceId(nb_sentence)).setAttribute('onclick',onclickFunction)
}

const ChangeSentenceLikeButtonToUnlike = function (nb_sentence) {
  const onclickFunction = 'UnlikeSentence(' + nb_sentence + ');';
  document.getElementById('like_'+nb_sentence).classList.add('liked');
  document.getElementById(getSentenceId(nb_sentence)).setAttribute('onclick',onclickFunction)
}

const GenerateSentence = function (sentence, nb_sentence, pict_id=null, has_pict=true, nb_likes=null) {
  const onclickFunction = 'LikeSentence(' + nb_sentence + ');';
  let res = '<div class="sentence" id="' + getSentenceId(nb_sentence) + '" onclick='+onclickFunction+'>';
  res += '<p>'+ sentence + '<\p>';

  if(!nb_likes){
    nb_likes= "";
  }
  if (has_pict) {
    res += '<div id=like_' + nb_sentence + ' class="heart" style="">'+nb_likes+'</div>';
  }
  res += '</div>';
  //console.log(res);
  return res;
}
