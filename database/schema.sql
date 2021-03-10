DROP DATABASE IF EXISTS db;

CREATE DATABASE db;

\c db;

CREATE TABLE "students" (
  "STUDENT" INTEGER PRIMARY KEY,
  "Name" VARCHAR
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
  "NAME" TEXT
);

CREATE TABLE "courses" (
  "COURSE" INTEGER PRIMARY KEY,
  "NAME" VARCHAR
);

CREATE TABLE "professors_teach" (
  "PROFESSOR" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("PROFESSOR", "COURSE")
);

CREATE TABLE "students_in" (
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
  "PROFESSOR" INTEGER,
  "NAME" VARCHAR,
  "PUBLIC" BOOLEAN,
  "NUM_CONVERSATION" INTEGER,
  "IS_FINISHED" BOOLEAN,
  "DATE_CREATED" DATE,
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

CREATE TABLE "stakeholder_page" (
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

CREATE TABLE "actions_taken" (
  "RESPONSE" INTEGER,
  "ACTION_PAGE" INTEGER
);

CREATE TABLE "scenarios_for" (
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("SCENARIO", "VERSION", "COURSE")
);

CREATE TABLE "issues" (
  "ISSUE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "NAME" TEXT,
  "IMPORTANCE_SCORE" INTEGER,
  PRIMARY KEY ("ISSUE", "SCENARIO", "VERSION")
);

CREATE TABLE "assigned_to" (
  "STUDENT" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  PRIMARY KEY ("STUDENT", "SCENARIO", "VERSION")
);

CREATE TABLE "student_times" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "DATE_TAKEN" DATE,
  "PAGE" INTEGER,
  "START_TIME" DATE,
  "END_TIME" DATE,
  PRIMARY KEY ("STUDENT", "COURSE", "SCENARIO", "VERSION", "DATE_TAKEN", "PAGE")
);

ALTER TABLE "students" ADD FOREIGN KEY ("STUDENT") REFERENCES "demographics" ("STUDENT");

ALTER TABLE "professors_teach" ADD FOREIGN KEY ("PROFESSOR") REFERENCES "professors" ("PROFESSOR");

ALTER TABLE "professors_teach" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "students_in" ADD FOREIGN KEY ("STUDENT") REFERENCES "students" ("STUDENT");

ALTER TABLE "students_in" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

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

ALTER TABLE "professors" ADD FOREIGN KEY ("PROFESSOR") REFERENCES "scenarios" ("PROFESSOR");

ALTER TABLE "stakeholders" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "stakeholders" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "coverage" ("STAKEHOLDER");

ALTER TABLE "coverage" ADD FOREIGN KEY ("ISSUE") REFERENCES "issues" ("ISSUE");

ALTER TABLE "pages" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "pages" ADD FOREIGN KEY ("NEXT_PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "conversations" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "stakeholders" ("STAKEHOLDER");

ALTER TABLE "reflection_questions" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "stakeholder_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "stakeholder_page" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "stakeholders" ("STAKEHOLDER");

ALTER TABLE "generic_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "action_page" ADD FOREIGN KEY ("PAGE") REFERENCES "pages" ("PAGE");

ALTER TABLE "actions_taken" ADD FOREIGN KEY ("RESPONSE") REFERENCES "responses" ("RESPONSE");

ALTER TABLE "actions_taken" ADD FOREIGN KEY ("ACTION_PAGE") REFERENCES "action_page" ("id");

ALTER TABLE "scenarios_for" ADD FOREIGN KEY ("COURSE") REFERENCES "courses" ("COURSE");

ALTER TABLE "scenarios_for" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "scenarios_for" ADD FOREIGN KEY ("VERSION") REFERENCES "scenarios" ("VERSION");

ALTER TABLE "issues" ADD FOREIGN KEY ("SCENARIO") REFERENCES "scenarios" ("SCENARIO");

ALTER TABLE "issues" ADD FOREIGN KEY ("VERSION") REFERENCES "scenarios" ("VERSION");

ALTER TABLE "students" ADD FOREIGN KEY ("STUDENT") REFERENCES "assigned_to" ("STUDENT");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("SCENARIO") REFERENCES "assigned_to" ("SCENARIO");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("VERSION") REFERENCES "assigned_to" ("VERSION");

ALTER TABLE "students" ADD FOREIGN KEY ("STUDENT") REFERENCES "student_times" ("STUDENT");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("SCENARIO") REFERENCES "student_times" ("SCENARIO");

ALTER TABLE "scenarios" ADD FOREIGN KEY ("VERSION") REFERENCES "student_times" ("VERSION");

ALTER TABLE "pages" ADD FOREIGN KEY ("PAGE") REFERENCES "student_times" ("PAGE");

