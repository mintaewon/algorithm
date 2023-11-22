-- 코드를 입력하세요
SELECT RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS, RR.SCORE
from REST_INFO RI
INNER JOIN (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE FROM REST_REVIEW GROUP BY REST_ID) RR
ON RI.REST_ID = RR.REST_ID
WHERE RI.ADDRESS LIKE '서울%'
ORDER BY RR.SCORE DESC, RI.FAVORITES DESC