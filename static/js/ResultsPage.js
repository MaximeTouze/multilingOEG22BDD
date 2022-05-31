/** function onload
  Called during the loading of the Result web page
*/
function onload() {
  // get the mostly liked sentences
$.ajax({
  type:'GET',
  url:'/mostly_liked_sentences',
  data:{},
  success:function(response)
  {
    // need display pannel to put the mostly liked sentences in
    var elt = document.getElementById('displayPanel');
    elt.innerHTML = '';
    const sentences = response.liked_sentences;
    const keys = Object.keys(sentences);

    // for each sentence
    for (var i = 0; i < keys.length; i++) {
      lang = keys[i];
      sent = sentences[lang];
      sentence_ = sent.sentence;
      likes = sent.nb_likes;
      // add the sentence to the showed sentences list
      elt.innerHTML += "<div class='sentence'><p>"+ sentence +"</p> <p class='nb_like'>"+ likes +" likes</p><p class='heart.liked'></p> </div>"
    }
  }
});
}
