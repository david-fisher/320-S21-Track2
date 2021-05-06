CREATE TABLE STUDENTS (
  STUDENT TEXT PRIMARY KEY,
  FNAME TEXT,
  LNAME TEXT
);

CREATE TABLE DEMOGRAPHICS (
  STUDENT TEXT PRIMARY KEY,
  AGE INTEGER,
  GRADE INTEGER,
  GENDER TEXT,
  RACE TEXT,
  MAJOR TEXT,
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT)
);

CREATE TABLE PROFESSORS (
  PROFESSOR TEXT PRIMARY KEY,
  FNAME TEXT,
  LNAME TEXT
);

CREATE TABLE SCENARIOS (
  SCENARIO INTEGER,
  VERSION INTEGER,
  NAME TEXT,
  PUBLIC BOOLEAN,
  NUM_CONVERSATION INTEGER,
  IS_FINISHED BOOLEAN,
  DATE_CREATED DATE,
  SCENARIO_ID SERIAL,
  PRIMARY KEY (SCENARIO_ID),
  UNIQUE (SCENARIO, VERSION)
);

CREATE TABLE COURSES (
  COURSE SERIAL PRIMARY KEY,
  NAME TEXT
);

CREATE TABLE PROFESSORS_TO_COURSES (
  PROFESSOR TEXT,
  COURSE INTEGER,
  ID SERIAL,
  PRIMARY KEY (ID),
  UNIQUE (PROFESSOR, COURSE),
  FOREIGN KEY (PROFESSOR) REFERENCES PROFESSORS (PROFESSOR),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE)
);

CREATE TABLE PROFESSORS_TO_SCENARIO (
  PROFESSOR TEXT,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  ID SERIAL PRIMARY KEY, 
  UNIQUE (PROFESSOR, SCENARIO),
  FOREIGN KEY (PROFESSOR) REFERENCES PROFESSORS (PROFESSOR),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE STUDENTS_TO_COURSE (
  STUDENT TEXT,
  COURSE INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (STUDENT, COURSE),
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE)
);

CREATE TABLE STUDENT_TIMES (
  STUDENT TEXT,
  COURSE INTEGER,
  SCENARIO_ID INTEGER,
  DATE_TAKEN DATE,
  PAGE INTEGER,
  START_TIME DATE,
  END_TIME DATE,
  ID SERIAL PRIMARY KEY,
  UNIQUE (STUDENT, COURSE, SCENARIO_ID, DATE_TAKEN, PAGE),
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE)
);

CREATE TABLE PAGES (
  PAGE INTEGER,
  PAGE_TYPE TEXT,
  PAGE_TITLE TEXT,
  SCENARIO INTEGER,
  VERSION INTEGER,
  BODY TEXT,
  NEXT_ID INTEGER,
  X_COORDINATE INTEGER,
  Y_COORDINATE INTEGER,
  COMPLETED BOOLEAN,
  ID SERIAL PRIMARY KEY,
  UNIQUE (PAGE, VERSION),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID),
  FOREIGN KEY (NEXT_ID) REFERENCES PAGES (ID)
);

CREATE TABLE PAGES_TO_SCENARIO (
  PAGE_ID INTEGER,
  SCENARIO_ID INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (PAGE_ID, SCENARIO_ID),
  FOREIGN KEY (PAGE_ID) REFERENCES PAGES (ID),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE RESPONSES (
  RESPONSE_ID SERIAL PRIMARY KEY,
  RESPONSE INTEGER,
  STUDENT TEXT,
  SCENARIO INTEGER,
  VERSION INTEGER,
  PAGE INTEGER,
  COURSE INTEGER,
  DATE_TAKEN DATE,
  CHOICE TEXT,
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID),
  FOREIGN KEY (PAGE) REFERENCES PAGES (ID),
  UNIQUE (RESPONSE, STUDENT, SCENARIO, PAGE, COURSE, DATE_TAKEN)
);

CREATE TABLE STAKEHOLDERS (
  STAKEHOLDER INTEGER,
  SCENARIO INTEGER,
  VERSION INTEGER,
  NAME TEXT,
  DESCRIPTION TEXT,
  JOB TEXT,
  INTRODUCTION TEXT,
  ENABLE_MULTI_CONVO BOOLEAN,
  ID SERIAL PRIMARY KEY,
  UNIQUE (STAKEHOLDER, VERSION),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE QUESTIONS (
  QUESTION INTEGER,
  VERSION INTEGER,
  POINTS INTEGER,
  QUESTION_TEXT TEXT,
  QUESTION_SUMMARY TEXT,
  ID SERIAL PRIMARY KEY,
  UNIQUE (QUESTION, VERSION)
);

CREATE TABLE STAKEHOLDERS_TO_QUESTIONS (
  STAKEHOLDER INTEGER,
  QUESTION INTEGER,
  ID SERIAL PRIMARY KEY,
  FOREIGN KEY (STAKEHOLDER) REFERENCES STAKEHOLDERS (ID),
  FOREIGN KEY (QUESTION) REFERENCES QUESTIONS (ID),
  UNIQUE (STAKEHOLDER, QUESTION)
);

CREATE TABLE REFLECTIONS_TAKEN (
  REFLECTIONS TEXT,
  RESPONSE_ID SERIAL PRIMARY KEY,
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID)
);

CREATE TABLE ISSUES (
  ISSUE SERIAL UNIQUE,
  SCENARIO_ID INTEGER,
  NAME TEXT,
  IMPORTANCE_SCORE INTEGER,
  PRIMARY KEY (ISSUE),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE COVERAGE (
  STAKEHOLDER INTEGER,
  ISSUE INTEGER,
  COVERAGE_SCORE DECIMAL,
  ID SERIAL PRIMARY KEY,
  UNIQUE (STAKEHOLDER, ISSUE),
  FOREIGN KEY (ISSUE) REFERENCES ISSUES (ISSUE),
  FOREIGN KEY (STAKEHOLDER) REFERENCES STAKEHOLDERS (ID)
);

CREATE TABLE CONVERSATIONS (
  CONVERSATION SERIAL PRIMARY KEY,
  STAKEHOLDER INTEGER,
  QUESTION TEXT,
  QUESTION_SUMMARY TEXT,
  POINTS INTEGER,
  RESPONSE TEXT,
  FOREIGN KEY (STAKEHOLDER) REFERENCES STAKEHOLDERS (ID)
);

CREATE TABLE RESPONSES_TO_CONVERSATIONS (
  RESPONSE_ID INTEGER,
  STAKEHOLDER INTEGER,
  STAKEHOLDER_VERSION INTEGER,
  SCORE DECIMAL,
  CONVERSATION INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (RESPONSE_ID, CONVERSATION),
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID),
  FOREIGN KEY (STAKEHOLDER) REFERENCES STAKEHOLDERS (ID),
  FOREIGN KEY (CONVERSATION) REFERENCES CONVERSATIONS (CONVERSATION)
);

CREATE TABLE REFLECTION_QUESTIONS (
  REFLECTION_QUESTION_ID INTEGER,
  REFLECTION_QUESTION TEXT,
  VERSION INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (REFLECTION_QUESTION_ID, VERSION)
);

CREATE TABLE REFLECTION_QUESTION_TO_PAGE (
  REFLECTION_QUESTION_ID INTEGER,
  PAGE_ID INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (REFLECTION_QUESTION_ID, PAGE_ID),
  FOREIGN KEY (REFLECTION_QUESTION_ID) REFERENCES REFLECTION_QUESTIONS (ID),
  FOREIGN KEY (PAGE_ID) REFERENCES PAGES (ID)
);

CREATE TABLE STAKEHOLDER_TO_PAGE (
  PAGE INTEGER,
  STAKEHOLDER INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (PAGE, STAKEHOLDER),
  FOREIGN KEY (PAGE) REFERENCES PAGES (ID),
  FOREIGN KEY (STAKEHOLDER) REFERENCES STAKEHOLDERS (ID)
);

CREATE TABLE GENERIC_PAGE (
  GENERIC_PAGE_ID INTEGER,
  PAGE INTEGER,
  BODY TEXT,
  VERSION INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (GENERIC_PAGE_ID, VERSION),
  FOREIGN KEY (PAGE) REFERENCES PAGES (ID)
);

CREATE TABLE ACTION_PAGE (
  ACTION_PAGE_ID INTEGER,
  PAGE INTEGER,
  VERSION INTEGER,
  CHOICE TEXT,
  RESULT_PAGE INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (ACTION_PAGE_ID, VERSION),
  FOREIGN KEY (PAGE) REFERENCES PAGES (ID)
);

CREATE TABLE RESPONSE_TO_ACTION_PAGE (
  RESPONSE_ID INTEGER,
  ACTION_PAGE INTEGER,
  ID SERIAL PRIMARY KEY,
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID),
  FOREIGN KEY (ACTION_PAGE) REFERENCES ACTION_PAGE (ID)
);

CREATE TABLE SCENARIOS_FOR (
  SCENARIO_ID INTEGER,
  VERSION INTEGER,
  COURSE INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (SCENARIO_ID, COURSE),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE COURSES_TO_SCENARIO (
  COURSE INTEGER,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  ID SERIAL PRIMARY KEY,
  UNIQUE (COURSE, SCENARIO),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);
