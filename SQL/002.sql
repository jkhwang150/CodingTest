-- 인기있는 아이스크림
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;


-- 흉부외과 또는 일반외과 의사 목록 출력하기
SELECT DR_NAME, DR_ID, MCDP_CD, TO_CHAR(HIRE_YMD,'YYYY-MM-DD') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC

-- 12세 이하인 여자 환자 목록 출력하기
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, "NONE") AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;