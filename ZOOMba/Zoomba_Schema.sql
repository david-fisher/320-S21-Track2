CREATE TABLE STUDENTS (
  STUDENT INTEGER PRIMARY KEY,
  FNAME TEXT,
  LNAME TEXT
);

CREATE TABLE DEMOGRAPHICS (
  STUDENT INTEGER PRIMARY KEY,
  AGE INTEGER,
  GRADE INTEGER,
  GENDER TEXT,
  RACE TEXT,
  MAJOR TEXT,
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT)
);

CREATE TABLE PROFESSORS (
  PROFESSOR INTEGER PRIMARY KEY,
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
  SCENARIO_ID INT,
  PRIMARY KEY (SCENARIO_ID),
  UNIQUE (SCENARIO, VERSION)
);

CREATE TABLE COURSES (
  COURSE INTEGER PRIMARY KEY,
  NAME TEXT
);

CREATE TABLE PROFESSORS_TO_COURSES (
  PROFESSOR INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (PROFESSOR, COURSE),
  FOREIGN KEY (PROFESSOR) REFERENCES PROFESSORS (PROFESSOR),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE)
);

CREATE TABLE PROFESSORS_TO_SCENARIO (
  PROFESSOR INTEGER,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  PRIMARY KEY (PROFESSOR, SCENARIO),
  FOREIGN KEY (PROFESSOR) REFERENCES PROFESSORS (PROFESSOR),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE STUDENTS_TO_COURSE (
  STUDENT INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (STUDENT, COURSE),
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE)
);

CREATE TABLE STUDENT_TIMES (
  STUDENT INTEGER,
  COURSE INTEGER,
  SCENARIO_ID INTEGER,
  DATE_TAKEN DATE,
  PAGE INTEGER,
  START_TIME DATE,
  END_TIME DATE,
  PRIMARY KEY (STUDENT, COURSE, SCENARIO_ID, DATE_TAKEN, PAGE),
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
  NEXT_PAGE INTEGER,
  NEXT_PAGE_VERSION INTEGER,
  X_COORDINATE INTEGER,
  Y_COORDINATE INTEGER,
  COMPLETED BOOLEAN,
  PRIMARY KEY (PAGE, VERSION),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID),
  FOREIGN KEY (NEXT_PAGE, NEXT_PAGE_VERSION) REFERENCES PAGES (PAGE, VERSION)
);

CREATE TABLE PAGES_TO_SCENARIO (
  PAGE_ID INTEGER,
  SCENARIO_ID INTEGER,
  PAGE_VERSION INTEGER,
  PRIMARY KEY (PAGE_ID, SCENARIO_ID, PAGE_VERSION),
  FOREIGN KEY (PAGE_ID, PAGE_VERSION) REFERENCES PAGES (PAGE, VERSION),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE RESPONSES (
  RESPONSE_ID INTEGER,
  RESPONSE INTEGER,
  STUDENT INTEGER,
  SCENARIO INTEGER,
  VERSION INTEGER,
  PAGE INTEGER,
  PAGE_VERSION INTEGER,
  COURSE INTEGER,
  DATE_TAKEN DATE,
  CHOICE TEXT,
  PRIMARY KEY (RESPONSE_ID),
  FOREIGN KEY (STUDENT) REFERENCES STUDENTS (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID),
  FOREIGN KEY (PAGE, PAGE_VERSION) REFERENCES PAGES (PAGE, VERSION),
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
  PRIMARY KEY(STAKEHOLDER, VERSION),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE QUESTIONS (
  QUESTION INTEGER,
  VERSION INTEGER,
  POINTS INTEGER,
  QUESTION_TEXT TEXT,
  PRIMARY KEY (QUESTION, QUESTION_VERSION)
);

CREATE TABLE STAKEHOLDERS_TO_QUESTIONS (
  STAKEHOLDER INTEGER, 
  STAKEHOLDER_VERSION INTEGER,
  QUESTION INTEGER,
  QUESTION_VERSION INTEGER,
  FOREIGN KEY (STAKEHOLDER, STAKEHOLDER_VERSION) REFERENCES STAKEHOLDERS (STAKEHOLDER, VERSION),
  FOREIGN KEY (QUESTION, QUESTION_VERSION) REFERENCES QUESTIONS (QUESTION, VERSION),
  PRIMARY KEY(STAKEHOLDER, STAKEHOLDER_VERSION, QUESTION, QUESTION_VERSION)
);

CREATE TABLE REFLECTIONS_TAKEN (
  REFLECTIONS TEXT,
  RESPONSE_ID INTEGER PRIMARY KEY,
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID)
);

CREATE TABLE ISSUES (
  ISSUE INTEGER UNIQUE,
  SCENARIO_ID INTEGER,
  NAME TEXT,
  IMPORTANCE_SCORE INTEGER,
  PRIMARY KEY (ISSUE),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE COVERAGE (
  STAKEHOLDER INTEGER,
  STAKEHOLDER_VERSION INTEGER,
  ISSUE INTEGER,
  COVERAGE_SCORE DECIMAL,
  PRIMARY KEY (STAKEHOLDER, ISSUE),
  FOREIGN KEY (ISSUE) REFERENCES ISSUES (ISSUE),
  FOREIGN KEY (STAKEHOLDER, STAKEHOLDER_VERSION) REFERENCES STAKEHOLDERS (STAKEHOLDER, VERSION)
);

CREATE TABLE CONVERSATIONS (
  CONVERSATION INTEGER,
  STAKEHOLDER INTEGER,
  STAKEHOLDER_VERSION INTEGER,
  QUESTION TEXT,
  RESPONSE TEXT,
  PRIMARY KEY (CONVERSATION),
  FOREIGN KEY (STAKEHOLDER, STAKEHOLDER_VERSION) REFERENCES STAKEHOLDERS (STAKEHOLDER, VERSION)
);

CREATE TABLE RESPONSES_TO_CONVERSATIONS (
  RESPONSE_ID INTEGER,
  STAKEHOLDER INTEGER,
  STAKEHOLDER_VERSION INTEGER,
  SCORE DECIMAL,
  CONVERSATION INTEGER,
  PRIMARY KEY (RESPONSE_ID, CONVERSATION),
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID),
  FOREIGN KEY (STAKEHOLDER, STAKEHOLDER_VERSION) REFERENCES STAKEHOLDERS (STAKEHOLDER, VERSION),
  FOREIGN KEY (CONVERSATION) REFERENCES CONVERSATIONS (CONVERSATION)
);

CREATE TABLE REFLECTION_QUESTIONS (
  ID INTEGER,
  REFLECTION_QUESTION TEXT,
  VERSION INTEGER,
  PRIMARY KEY (ID, VERSION)
);

CREATE TABLE REFLECTION_QUESTION_TO_PAGE (
  REFLECTION_QUESTION_ID INTEGER,
  PAGE_ID INTEGER,
  REFLECTION_QUESTION_VERSION INTEGER,
  PAGE_VERSION INTEGER,
  PRIMARY KEY (REFLECTION_QUESTION_ID, PAGE_ID, REFLECTION_QUESTION_VERSION, PAGE_VERSION),
  FOREIGN KEY (REFLECTION_QUESTION_ID, REFLECTION_QUESTION_VERSION) REFERENCES REFLECTION_QUESTIONS (ID, VERSION),
  FOREIGN KEY (PAGE_ID, PAGE_VERSION) REFERENCES PAGES (PAGE, VERSION)
);

CREATE TABLE STAKEHOLDER_TO_PAGE (
  PAGE INTEGER,
  PAGE_VERSION INTEGER,
  STAKEHOLDER INTEGER,
  STAKEHOLDER_VERSION INTEGER,
  PRIMARY KEY (PAGE, PAGE_VERSION, STAKEHOLDER, STAKEHOLDER_VERSION),
  FOREIGN KEY (PAGE, PAGE_VERSION) REFERENCES PAGES (PAGE, VERSION),
  FOREIGN KEY (STAKEHOLDER, STAKEHOLDER_VERSION) REFERENCES STAKEHOLDERS (STAKEHOLDER, VERSION)
);

CREATE TABLE GENERIC_PAGE (
  ID INTEGER,
  PAGE INTEGER,
  BODY TEXT,
  VERSION INTEGER,
  PRIMARY KEY (ID, VERSION),
  FOREIGN KEY (PAGE, VERSION) REFERENCES PAGES (PAGE, VERSION)
);

CREATE TABLE ACTION_PAGE (
  ID INTEGER UNIQUE,
  PAGE INTEGER,
  VERSION INTEGER,
  CHOICE TEXT,
  RESULT_PAGE INTEGER,
  PRIMARY KEY (ID, VERSION),
  FOREIGN KEY (PAGE, VERSION) REFERENCES PAGES (PAGE, VERSION)
);

CREATE TABLE RESPONSE_TO_ACTION_PAGE (
  RESPONSE_ID INTEGER,
  ACTION_PAGE INTEGER,
  ACTION_PAGE_VERSION INTEGER,
  FOREIGN KEY (RESPONSE_ID) REFERENCES RESPONSES (RESPONSE_ID),
  FOREIGN KEY (ACTION_PAGE, ACTION_PAGE_VERSION) REFERENCES ACTION_PAGE (ID, VERSION)
);

CREATE TABLE SCENARIOS_FOR (
  SCENARIO_ID INTEGER,
  VERSION INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (SCENARIO_ID, COURSE),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO_ID) REFERENCES SCENARIOS (SCENARIO_ID)
);

CREATE TABLE COURSES_TO_SCENARIO (
  COURSE INTEGER,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  PRIMARY KEY (COURSE, SCENARIO),
  FOREIGN KEY (COURSE) REFERENCES COURSES (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES SCENARIOS (SCENARIO_ID)
);
