$.ajax({
  type:'GET',
  url:'/mostly_liked_sentences',
  data:'',
  success:function(response)
  {
    var elt = document.getElementById('displayPanel');
    elt.innerHTML = '';
    const sentences = response.liked_sentences;
    const keys = Object.keys(sentences);

    for (var i = 0; i < keys.length; i++) {
      lang = keys[i];
      sent = sentences[lang];
      sentence_ = sent.sentence;
      likes = sent.nb_likes;
      elt.innerHTML += "<div class='sentence'><p>"+ sentence +"</p> <p class='nb_like'>"+ likes +" likes</p><p class='heart.liked'></p> </div>"
      //sentences = sentences.concat(sentences_[sentence_rank]);
    }
  }
});
