CREATE TABLE students (
  STUDENT INTEGER PRIMARY KEY,
  FNAME TEXT,
  LNAME TEXT
);

CREATE TABLE demographics (
  STUDENT INTEGER PRIMARY KEY,
  AGE INTEGER,
  GRADE INTEGER,
  GENDER TEXT,
  RACE TEXT,
  MAJOR TEXT,
  FOREIGN KEY (STUDENT) REFERENCES demographics (STUDENT)
);

CREATE TABLE professors (
  PROFESSOR INTEGER PRIMARY KEY,
  FNAME TEXT,
  LNAME TEXT
);

CREATE TABLE scenarios (
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

CREATE TABLE courses (
  COURSE INTEGER PRIMARY KEY,
  NAME TEXT
);

CREATE TABLE professors_to_courses (
  PROFESSOR INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (PROFESSOR, COURSE),
  FOREIGN KEY (PROFESSOR) REFERENCES professors (PROFESSOR),
  FOREIGN KEY (COURSE) REFERENCES courses (COURSE)
);

CREATE TABLE professors_to_scenario (
  PROFESSOR INTEGER,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  PRIMARY KEY (PROFESSOR, SCENARIO),
  FOREIGN KEY (PROFESSOR) REFERENCES professors (PROFESSOR),
  FOREIGN KEY (SCENARIO) REFERENCES scenarios (SCENARIO)
);

CREATE TABLE students_to_course (
  STUDENT INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (STUDENT, COURSE),
  FOREIGN KEY (STUDENT) REFERENCES students (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES courses (COURSE)
);

CREATE TABLE student_times (
  STUDENT INTEGER,
  COURSE INTEGER,
  SCENARIO_ID INTEGER,
  DATE_TAKEN DATE,
  PAGE INTEGER,
  START_TIME DATE,
  END_TIME DATE,
  PRIMARY KEY (STUDENT, COURSE, SCENARIO_ID, DATE_TAKEN, PAGE),
  FOREIGN KEY (STUDENT) REFERENCES students (STUDENT),
  FOREIGN KEY (SCENARIO_ID) REFERENCES scenarios (SCENARIO_ID),
  FOREIGN KEY (COURSE) REFERENCES courses (COURSE)
);

CREATE TABLE student_page_progress (
  STUDENT INTEGER,
  PAGE INTEGER,
  COMPLETED BOOLEAN,
  PRIMARY KEY (STUDENT, PAGE)
);

CREATE TABLE pages (
  PAGE INTEGER UNIQUE,
  PAGE_TYPE TEXT,
  PAGE_TITLE TEXT,
  SCENARIO INTEGER,
  VERSION INTEGER,
  BODY TEXT,
  NEXT_PAGE INTEGER,
  X_COORDINATE INTEGER,
  Y_COORDINATE INTEGER,
  PRIMARY KEY (PAGE, SCENARIO, VERSION),
  FOREIGN KEY (SCENARIO) REFERENCES scenarios (SCENARIO),
  FOREIGN KEY (NEXT_PAGE) REFERENCES pages (PAGE)
);

CREATE TABLE responses (
  RESPONSE_ID INTEGER UNIQUE,
  RESPONSE INTEGER,
  STUDENT INTEGER,
  SCENARIO INTEGER,
  VERSION INTEGER,
  PAGE INTEGER,
  COURSE INTEGER,
  DATE_TAKEN DATE,
  CHOICE TEXT,
  PRIMARY KEY (RESPONSE, STUDENT, SCENARIO, VERSION, PAGE, COURSE, DATE_TAKEN),
  FOREIGN KEY (STUDENT) REFERENCES students (STUDENT),
  FOREIGN KEY (COURSE) REFERENCES courses (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES scenarios (SCENARIO),
  FOREIGN KEY (PAGE) REFERENCES pages (PAGE)
);

CREATE TABLE stakeholders (
  STAKEHOLDER INTEGER PRIMARY KEY,
  SCENARIO INTEGER,
  VERSION INTEGER,
  NAME TEXT,
  DESCRIPTION TEXT,
  JOB TEXT,
  INTRODUCTION TEXT,
  FOREIGN KEY (SCENARIO) REFERENCES scenarios (SCENARIO)
);

CREATE TABLE reflections_taken (
  REFLECTIONS TEXT,
  RESPONSE_ID INTEGER PRIMARY KEY,
  FOREIGN KEY (RESPONSE_ID) REFERENCES responses (RESPONSE_ID)
);

CREATE TABLE issues (
  ISSUE INTEGER UNIQUE,
  SCENARIO_ID INTEGER,
  NAME TEXT,
  IMPORTANCE_SCORE INTEGER,
  PRIMARY KEY (ISSUE, SCENARIO_ID),
  FOREIGN KEY (SCENARIO_ID) REFERENCES scenarios (SCENARIO_ID)
);

CREATE TABLE coverage (
  STAKEHOLDER INTEGER,
  ISSUE INTEGER,
  COVERAGE_SCORE DECIMAL,
  PRIMARY KEY (STAKEHOLDER, ISSUE),
  FOREIGN KEY (ISSUE) REFERENCES issues (ISSUE),
  FOREIGN KEY (STAKEHOLDER) REFERENCES stakeholders (STAKEHOLDER)
);

CREATE TABLE conversations (
  CONVERSATION INTEGER,
  STAKEHOLDER INTEGER,
  QUESTION TEXT,
  RESPONSE TEXT,
  PRIMARY KEY (CONVERSATION, STAKEHOLDER),
  FOREIGN KEY (STAKEHOLDER) REFERENCES stakeholders (STAKEHOLDER)
);

CREATE TABLE responses_to_conversations (
  RESPONSE_ID INTEGER,
  STAKEHOLDER INTEGER,
  SCORE DECIMAL,
  CONVERSATION INTEGER,
  PRIMARY KEY (RESPONSE_ID, CONVERSATION),
  FOREIGN KEY (RESPONSE_ID) REFERENCES responses (RESPONSE_ID),
  FOREIGN KEY (STAKEHOLDER) REFERENCES stakeholders (STAKEHOLDER),
  FOREIGN KEY (CONVERSATION, STAKEHOLDER) REFERENCES conversations (CONVERSATION, STAKEHOLDER)
);

CREATE TABLE reflection_questions (
  id INTEGER,
  PAGE INTEGER,
  REFLECTION_QUESTION TEXT,
  PRIMARY KEY (id, PAGE, REFLECTION_QUESTION),
  FOREIGN KEY (PAGE) REFERENCES pages (PAGE)
);

CREATE TABLE stakeholder_to_page (
  PAGE INTEGER,
  STAKEHOLDER INTEGER,
  PRIMARY KEY (PAGE, STAKEHOLDER),
  FOREIGN KEY (PAGE) REFERENCES pages (PAGE),
  FOREIGN KEY (STAKEHOLDER) REFERENCES stakeholders (STAKEHOLDER)
);

CREATE TABLE generic_page (
  id INTEGER,
  PAGE INTEGER,
  BODY TEXT,
  PRIMARY KEY (id, PAGE, BODY),
  FOREIGN KEY (PAGE) REFERENCES pages (PAGE)
);

CREATE TABLE action_page (
  id INTEGER UNIQUE,
  PAGE INTEGER,
  CHOICE TEXT,
  RESULT_PAGE INTEGER,
  PRIMARY KEY (id, PAGE, CHOICE),
  FOREIGN KEY (PAGE) REFERENCES pages (PAGE)
);

CREATE TABLE response_to_action_page (
  RESPONSE_ID INTEGER,
  ACTION_PAGE INTEGER,
  FOREIGN KEY (RESPONSE_ID) REFERENCES responses (RESPONSE_ID),
  FOREIGN KEY (ACTION_PAGE) REFERENCES action_page (id)
);

CREATE TABLE scenarios_for (
  SCENARIO_ID INTEGER,
  COURSE INTEGER,
  PRIMARY KEY (SCENARIO_ID, COURSE),
  FOREIGN KEY (COURSE) REFERENCES courses (COURSE),
  FOREIGN KEY (SCENARIO_ID) REFERENCES scenarios (SCENARIO_ID)
);

CREATE TABLE courses_to_scenario (
  COURSE INTEGER,
  SCENARIO INTEGER,
  PERMISSION INTEGER,
  PRIMARY KEY (COURSE, SCENARIO),
  FOREIGN key (COURSE) REFERENCES courses (COURSE),
  FOREIGN KEY (SCENARIO) REFERENCES scenarios (SCENARIO)
);