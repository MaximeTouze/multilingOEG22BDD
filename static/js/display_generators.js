// Generate the html parts
// sentence separator
const SENTENCE_SEPARATOR = "___________________";

// Generate an img
const GenerateImg = function (path, alt, style="", onclick=null, id=null) {
  let img = "<img style='" + style + "' src=\"" + path + "\" alt='" + alt
  // if there is an id to put on the img
  if (id) {
    img += "' id='" + id;
  } // if an onclick must be added
  if (onclick) {
    img += "' onclick='" + onclick;
  }// return the result
  return img + "'>";
}

// returns an img in exposed folder
const GenerateExposedImg = function (name, style="weight:100%; height:100%", onclick=null, id=null) {
  return GenerateImg("../static/exposed/" + name, name, style=style, onclick=onclick, id);
}

// changes the dislike button to like
const ChangeSentenceDislikeButtonToLike = function (nb_sentence) {
  const onclickFunction = 'LikeSentence(' + nb_sentence + ');';
  document.getElementById('like_'+nb_sentence).classList.remove('liked');
  document.getElementById(getSentenceId(nb_sentence)).setAttribute('onclick',onclickFunction)
}

// changes the like button to not liked status
const ChangeSentenceLikeButtonToUnlike = function (nb_sentence) {
  const onclickFunction = 'UnlikeSentence(' + nb_sentence + ');';
  document.getElementById('like_'+nb_sentence).classList.add('liked');
  document.getElementById(getSentenceId(nb_sentence)).setAttribute('onclick',onclickFunction)
}

// generate a sentence
const GenerateSentence = function (sentence, nb_sentence, pict_id=null, has_pict=true, nb_likes=null) {
  const onclickFunction = 'LikeSentence(' + nb_sentence + ');';
  let res = '<div class="sentence" id="' + getSentenceId(nb_sentence) + '" onclick='+onclickFunction+'>';
  res += '<p>'+ sentence + '<\p>';
  // if no likes, don t diplay the numbers
  if(!nb_likes){
    nb_likes= "";
  }
  // If sentence has a pict to show
  if (has_pict) {
    res += '<div id=like_' + nb_sentence + ' class="heart" style="">'+nb_likes+'</div>';
  }
  res += '</div>';
  //console.log(res);
  return res;
}
