desc emp;
select ename,empno,job from emp;

select * from emp;

select ename,sal from emp;

select * from emp where deptno=30;

select * from emp where sal>1600 or ename="SMITH";

select * from emp where sal <> 2850;

select * from emp order by sal DESC;

select DISTINCT job from emp;

select * from emp limit 4;

select * from emp;

SELECT * from dept;

select emp.empno,dept.loc from emp inner join dept on emp.deptno=dept.deptno;

select job,sum(sal) as total_sal from emp group by job having total_sal>5000;

select empno,ename, ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal DESC) as sal_rank from emp;





# events - user_id, event_time,event_type,page,revenue

-- Rules 
    -- 1. A new session starts if the gap between two consective events of the same user is  > 30 min. 
    -- 2. For each session : return
        -- user_id 
        -- session_id (incrementing per user)
        -- session_start,session_end 
        -- event_count
        -- unique_pages 
        -- session_revenue 
        -- session_duration_seconds 



    user id         event_time          page        reveneu
    101                 10:00           home            0 
    101                 10:05           product         0 
    101                 10:50           checkout       200 
    101                 11:00.          home            0

A session :  Group of events that belong to one continious yser activity. 


10:00 
10:05
10:50 -> Gap > 30 mins -> new session 
11:00

Session 1 [10:00-10:05]
session 2 [10:50-11:00]

user id     session id 
101         1 
101         2 

This means :

    -- Each time new session dected increment counter 


Rule 3 : 

cutomers 
1
2
3
4

orders 
2
4

anti join 
1
3
