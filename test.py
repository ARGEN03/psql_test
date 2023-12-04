"=1="

# select plaintext from wordform limit 10;

"=2="

# select plaintext from wordform where plaintext ILIKE 'a%';

"=3="

# select title,genretype from work where genretype = 'p';

"=4="

# select  avg(totalparagraphs) as avg from work where genretype = 't';

"=5="

# select title from work where totalwords > (select avg(totalwords ) from work);

"=6="

# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid  

"=7="

# select round(avg(speechcount)) as round, work.title from character join character_work on character.charid = character_work.charid join work on character_work.workid=work.workid where work.title = 'Romeo and Juliet' group by work.title;
    
"=8="

# select section, sum(wordcount) as sum from paragraph group by section;

"=9="

# select  charname, speechcount from character where speechcount between 15 and 30;

"=10="

# SELECT title, year FROM work WHERE year between 1601 and 1699;

