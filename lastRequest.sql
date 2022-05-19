/* SHOW MUST LIKED IN ARABIC*/
SELECT Sentence.id, Sentence.arabic 
FROM Sentence 
INNER JOIN Likes ON Sentence.id = Likes.sentence_id 
WHERE Likes.arabic_like = 
    (SELECT MAX(Likes.arabic_like) FROM Likes);

/* SHOW MUST LIKED IN FRENCH*/
SELECT Sentence.id, Sentence.french 
FROM Sentence 
INNER JOIN Likes ON Sentence.id = Likes.sentence_id 
WHERE Likes.french_like = 
    (SELECT MAX(Likes.french_like) FROM Likes);

/* SHOW MUST LIKED IN ENGLISH*/
SELECT Sentence.id, Sentence.english 
FROM Sentence 
INNER JOIN Likes ON Sentence.id = Likes.sentence_id 
WHERE Likes.english_like = 
    (SELECT MAX(Likes.english_like) FROM Likes);

/* SHOW MUST LIKED IN SPANISH*/
SELECT Sentence.id, Sentence.spanish 
FROM Sentence 
INNER JOIN Likes ON Sentence.id = Likes.sentence_id 
WHERE Likes.spanish_like = 
    (SELECT MAX(Likes.spanish_like) FROM Likes);
