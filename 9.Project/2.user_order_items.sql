SELECT u.id, u.name, s.name, i.name FROM users u JOIN orders o ON u.id=o.userid JOIN stores s ON o.storeid=s.id JOIN orderitems oi ON o.id=oi.orderid JOIN items i ON oi.itemid = i.id WHERE u.id="6da2aec9-5aa2-4cc4-aba1-df81cef0cc02";
SELECT DISTINCT i.name FROM users u JOIN orders o ON u.id=o.userid JOIN orderitems oi ON o.id=oi.orderid JOIN items i ON oi.itemid = i.id WHERE u.id="6da2aec9-5aa2-4cc4-aba1-df81cef0cc02";
SELECT name,age from users WHERE age LIKE '2%';
SELECT SUM(i.unitprice) FROM users u JOIN orders o ON u.id=o.userid JOIN orderitems oi ON o.id=oi.orderid JOIN items i ON oi.itemid = i.id WHERE u.id="6da2aec9-5aa2-4cc4-aba1-df81cef0cc02";
SELECT o.userid, SUM(CAST(i.unitprice AS INTEGER)) AS revenue FROM users u JOIN orders o ON u.id=o.userid JOIN orderitems oi ON o.id=oi.orderid JOIN items i ON oi.itemid = i.id GROUP BY o.userid ORDER BY revenue DESC LIMIT 5;

SELECT * FROM users WHERE birthdate BETWEEN '2000-01-01' AND '2000-01-31';
SELECT * FROM users WHERE birthdate <= '2000-01-01';

SELECT * FROM users WHERE strftime('%m',BirthDate)='06';   -- 빌트인 함수 strftime  %m -> 월
SELECT * FROM users WHERE strftime('%d',BirthDate)='24';   -- 빌트인 함수 strftime  %d -> 일
                                                           -- 빌트인 함수 strftime  %Y -> 년