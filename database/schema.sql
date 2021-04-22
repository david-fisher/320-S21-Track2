DROP DATABASE IF EXISTS db;

CREATE DATABASE db;

\c db;

CREATE TABLE "students" (
  "STUDENT" INTEGER PRIMARY KEY,
  "FNAME" VARCHAR,
  "LNAME" VARCHAR
);

CREATE TABLE "demographics" (
  "STUDENT" INTEGER PRIMARY KEY,
  "AGE" INTEGER,
  "GRADE" VARCHAR,
  "GENDER" VARCHAR,
  "RACE" VARCHAR,
  "MAJOR" VARCHAR
);

CREATE TABLE "professors" (
  "PROFESSOR" INTEGER PRIMARY KEY,
  "FNAME" VARCHAR,
  "LNAME" VARCHAR
);

CREATE TABLE "courses" (
  "COURSE" INTEGER PRIMARY KEY,
  "NAME" VARCHAR
);

CREATE TABLE "professors_to_courses" (
  "PROFESSOR" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("PROFESSOR", "COURSE")
);

CREATE TABLE "professors_to_scenario" (
  "PROFESSOR" INTEGER,
  "SCENARIO" INTEGER,
  "PERMISSION" INTEGER,
  PRIMARY KEY ("PROFESSOR", "SCENARIO")
);

CREATE TABLE "students_to_course" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("STUDENT", "COURSE")
);

CREATE TABLE "responses" (
  "RESPONSE" INTEGER,
  "STUDENT" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "PAGE" INTEGER,
  "COURSE" INTEGER,
  "DATE_TAKEN" DATE,
  "CHOICE" TEXT,
  PRIMARY KEY ("RESPONSE", "STUDENT", "SCENARIO", "VERSION", "PAGE", "COURSE", "DATE_TAKEN")
);

CREATE TABLE "reflections_taken" (
  "REFLECTIONS" TEXT,
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "DATE_TAKEN" DATE,
  "PAGE" INTEGER,
  PRIMARY KEY ("REFLECTIONS", "STUDENT", "COURSE", "SCENARIO", "VERSION", "DATE_TAKEN")
);

CREATE TABLE "conversations_had" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "DATE_TAKEN" DATE,
  "STAKEHOLDER" INTEGER,
  "SCORE" DECIMAL,
  "CONVERSATION" INTEGER
);

CREATE TABLE "scenarios" (
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "NAME" VARCHAR,
  "PUBLIC" BOOLEAN,
  "NUM_CONVERSATION" INTEGER,
  "IS_FINISHED" BOOLEAN,
  "DATE_CREATED" DATE,
  "SCENARIO_HASH" INT UNIQUE,
  PRIMARY KEY ("SCENARIO", "VERSION")
);

CREATE TABLE "stakeholders" (
  "STAKEHOLDER" INTEGER PRIMARY KEY,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "NAME" TEXT,
  "DESCRIPTION" TEXT,
  "JOB" TEXT,
  "INTRODUCTION" TEXT
);

CREATE TABLE "coverage" (
  "STAKEHOLDER" INTEGER,
  "ISSUE" INTEGER,
  "COVERAGE_SCORE" DECIMAL,
  PRIMARY KEY ("STAKEHOLDER", "ISSUE")
);

CREATE TABLE "pages" (
  "PAGE" INTEGER,
  "PAGE_TYPE" VARCHAR,
  "PAGE_TITLE" TEXT,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "BODY" TEXT,
  "NEXT_PAGE" INTEGER,
  "X_COORDINATE" INTEGER,
  "Y_COORDINATE" INTEGER,
  PRIMARY KEY ("PAGE", "SCENARIO", "VERSION")
);

CREATE TABLE "conversations" (
  "CONVERSATION" INTEGER,
  "STAKEHOLDER" INTEGER,
  "QUESTION" TEXT,
  "RESPONSE" TEXT,
  PRIMARY KEY ("CONVERSATION", "STAKEHOLDER")
);

CREATE TABLE "reflection_questions" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "REFLECTION_QUESTION" TEXT,
  PRIMARY KEY ("id", "PAGE", "REFLECTION_QUESTION")
);

CREATE TABLE "stakeholder_to_page" (
  "PAGE" INTEGER,
  "STAKEHOLDER" INTEGER,
  PRIMARY KEY ("PAGE", "STAKEHOLDER")
);

CREATE TABLE "generic_page" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "BODY" TEXT,
  PRIMARY KEY ("id", "PAGE", "BODY")
);

CREATE TABLE "action_page" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "CHOICE" TEXT,
  "RESULT_PAGE" INTEGER,
  PRIMARY KEY ("id", "PAGE", "CHOICE")
);

CREATE TABLE "response_to_action_page" (
  "RESPONSE" INTEGER,
  "ACTION_PAGE" INTEGER
);

CREATE TABLE "scenarios_for" (
  "SCENARIO_HASH" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("SCENARIO_HASH", "COURSE")
);

CREATE TABLE "issues" (
  "ISSUE" INTEGER,
  "SCENARIO_HASH" INTEGER,
  "NAME" TEXT,
  "IMPORTANCE_SCORE" INTEGER,
  PRIMARY KEY ("ISSUE", "SCENARIO_HASH")
);

CREATE TABLE "student_times" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO_HASH" INTEGER,
  "DATE_TAKEN" DATE,
  "PAGE" INTEGER,
  "START_TIME" DATE,
  "END_TIME" DATE,
  PRIMARY KEY ("STUDENT", "COURSE", "SCENARIO_HASH", "DATE_TAKEN", "PAGE")
);

CREATE TABLE "courses_to_scenario" (
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "PERMISSION" INTEGER,
  PRIMARY KEY ("COURSE", "SCENARIO")
);

ALTER TABLE "students" ADD FOREIGN KEY ("STUDENT") REFERENCES "demographics" ("STUDENT");

ALTER TABLE "professors_to_courses" ADD FOREIGN KEY ("PROFESSOR") REFERENCES "professors" ("PROFESSOR");

ALTER TABLE "professors_to_courses" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "professors_to_scenario" ADD FOREIGN KEY ("PROFESSOR") REFERENCES "professors" ("PROFESSOR");

ALTER TABLE "professors_to_scenario" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "students_to_course" ADD FOREIGN KEY ("STUDENT") REFERENCES "students" ("STUDENT");

ALTER TABLE "students_to_course" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "responses" ADD FOREIGN KEY ("STUDENT") REFERENCES "students" ("STUDENT");

ALTER TABLE "responses" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "responses" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "responses" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "reflections_taken" ADD FOREIGN KEY ("STUDENT") REFERENCES "responses" ("STUDENT");

ALTER TABLE "reflections_taken" ADD FOREIGN KEY ("COURSE") REFERENCES "responses" ("COURSE");

ALTER TABLE "reflections_taken" ADD FOREIGN KEY ("SCENARIO") REFERENCES "responses" ("SCENARIO");

ALTER TABLE "reflections_taken" ADD FOREIGN KEY ("DATE_TAKEN") REFERENCES "responses" ("DATE_TAKEN");

ALTER TABLE "conversations_had" ADD FOREIGN KEY ("STUDENT") REFERENCES "responses" ("STUDENT");

ALTER TABLE "conversations_had" ADD FOREIGN KEY ("COURSE") REFERENCES "responses" ("COURSE");

ALTER TABLE "conversations_had" ADD FOREIGN KEY ("SCENARIO") REFERENCES "responses" ("SCENARIO");

ALTER TABLE "conversations_had" ADD FOREIGN KEY ("DATE_TAKEN") REFERENCES "responses" ("DATE_TAKEN");

ALTER TABLE "conversations_had" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "stakeholders" ("STAKEHOLDER");

ALTER TABLE "stakeholders" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "stakeholders" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "coverage" ("STAKEHOLDER");

ALTER TABLE "coverage" ADD FOREIGN KEY ("ISSUE") REFERENCES "issues" ("ISSUE");

ALTER TABLE "pages" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "pages" ADD FOREIGN KEY ("NEXT_PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "conversations" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "stakeholders" ("STAKEHOLDER");

ALTER TABLE "reflection_questions" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "stakeholder_to_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "stakeholder_to_page" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "stakeholders" ("STAKEHOLDER");

ALTER TABLE "generic_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "action_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "response_to_action_page" ADD FOREIGN KEY ("RESPONSE") REFERENCES "responses" ("RESPONSE");

ALTER TABLE "response_to_action_page" ADD FOREIGN KEY ("ACTION_PAGE") REFERENCES "action_page" ("id");

ALTER TABLE "scenarios_for" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "scenarios_for" ADD FOREIGN KEY ("SCENARIO_HASH") REFERENCES "scenarios" ("SCENARIO_HASH");

ALTER TABLE "issues" ADD FOREIGN KEY ("SCENARIO_HASH") REFERENCES "scenarios" ("SCENARIO_HASH");

ALTER TABLE "students" ADD FOREIGN KEY ("STUDENT") REFERENCES "student_times" ("STUDENT");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("SCENARIO_HASH") REFERENCES "student_times" ("SCENARIO_HASH");

ALTER TABLE "pages" ADD FOREIGN KEY ("PAGE") REFERENCES "student_times" ("PAGE");

ALTER TABLE "professors_to_courses" ADD FOREIGN KEY ("COURSE") REFERENCES "courses_to_scenario" ("COURSE");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("SCENARIO") REFERENCES "courses_to_scenario" ("SCENARIO");

ALTER TABLE "student_times" ADD FOREIGN KEY ("DATE_TAKEN") REFERENCES "action_page" ("CHOICE");

