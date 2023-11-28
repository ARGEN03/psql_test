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