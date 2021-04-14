DROP DATABASE IF EXISTS db;

CREATE DATABASE db;

\c db;

CREATE TABLE "tables_students" (
  "STUDENT" INTEGER PRIMARY KEY,
  "Name" VARCHAR
);

CREATE TABLE "tables_demographics" (
  "STUDENT" INTEGER PRIMARY KEY,
  "AGE" INTEGER,
  "GRADE" VARCHAR,
  "GENDER" VARCHAR,
  "RACE" VARCHAR,
  "MAJOR" VARCHAR
);

CREATE TABLE "tables_professors" (
  "PROFESSOR_id" INTEGER PRIMARY KEY,
  "NAME" TEXT
);

CREATE TABLE "tables_courses" (
  "COURSE" INTEGER PRIMARY KEY,
  "NAME" VARCHAR
);

CREATE TABLE "tables_professors_teach" (
  "PROFESSOR_id" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("PROFESSOR_id", "COURSE")
);

CREATE TABLE "tables_students_in" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("STUDENT", "COURSE")
);

CREATE TABLE "tables_responses" (
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

CREATE TABLE "tables_reflections_taken" (
  "REFLECTIONS" TEXT,
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "DATE_TAKEN" DATE,
  "PAGE" INTEGER,
  PRIMARY KEY ("REFLECTIONS", "STUDENT", "COURSE", "SCENARIO", "VERSION", "DATE_TAKEN")
);

CREATE TABLE "tables_conversations_had" (
  "STUDENT" INTEGER,
  "COURSE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "DATE_TAKEN" DATE,
  "STAKEHOLDER" INTEGER,
  "SCORE" DECIMAL,
  "CONVERSATION" INTEGER
);

CREATE TABLE "tables_scenarios" (
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "PROFESSOR_id" INTEGER,
  "NAME" VARCHAR,
  "PUBLIC" BOOLEAN,
  "NUM_CONVERSATION" INTEGER,
  "IS_FINISHED" BOOLEAN,
  "DATE_CREATED" DATE,
  PRIMARY KEY ("SCENARIO", "VERSION")
);

CREATE TABLE "tables_stakeholders" (
  "STAKEHOLDER" INTEGER PRIMARY KEY,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "NAME" TEXT,
  "DESCRIPTION" TEXT,
  "JOB" TEXT,
  "INTRODUCTION" TEXT
);

CREATE TABLE "tables_coverage" (
  "STAKEHOLDER" INTEGER,
  "ISSUE" INTEGER,
  "COVERAGE_SCORE" DECIMAL,
  PRIMARY KEY ("STAKEHOLDER", "ISSUE")
);

CREATE TABLE "tables_pages" (
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

CREATE TABLE "tables_conversations" (
  "CONVERSATION" INTEGER,
  "STAKEHOLDER" INTEGER,
  "QUESTION" TEXT,
  "RESPONSE" TEXT,
  PRIMARY KEY ("CONVERSATION", "STAKEHOLDER")
);

CREATE TABLE "tables_reflection_questions" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "REFLECTION_QUESTION" TEXT,
  PRIMARY KEY ("id", "PAGE", "REFLECTION_QUESTION")
);

CREATE TABLE "tables_stakeholder_page" (
  "PAGE" INTEGER,
  "STAKEHOLDER" INTEGER,
  PRIMARY KEY ("PAGE", "STAKEHOLDER")
);

CREATE TABLE "tables_generic_page" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "BODY" TEXT,
  PRIMARY KEY ("id", "PAGE", "BODY")
);

CREATE TABLE "tables_action_page" (
  "id" INTEGER,
  "PAGE" INTEGER,
  "CHOICE" TEXT,
  "RESULT_PAGE" INTEGER,
  PRIMARY KEY ("id", "PAGE", "CHOICE")
);

CREATE TABLE "tables_actions_taken" (
  "RESPONSE" INTEGER,
  "ACTION_PAGE" INTEGER
);

CREATE TABLE "tables_scenarios_for" (
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "COURSE" INTEGER,
  PRIMARY KEY ("SCENARIO", "VERSION", "COURSE")
);

CREATE TABLE "tables_issues" (
  "ISSUE" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  "NAME" TEXT,
  "IMPORTANCE_SCORE" INTEGER,
  PRIMARY KEY ("ISSUE", "SCENARIO", "VERSION")
);

CREATE TABLE "tables_assigned_to" (
  "STUDENT" INTEGER,
  "SCENARIO" INTEGER,
  "VERSION" INTEGER,
  PRIMARY KEY ("STUDENT", "SCENARIO", "VERSION")
);

CREATE TABLE "tables_student_times" (
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

ALTER TABLE "tables_students" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_demographics" ("STUDENT");

ALTER TABLE "tables_professors_teach" ADD FOREIGN KEY ("PROFESSOR_id") REFERENCES "tables_professors" ("PROFESSOR_id");

ALTER TABLE "tables_professors_teach" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_courses" ("COURSE");

ALTER TABLE "tables_students_in" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_students" ("STUDENT");

ALTER TABLE "tables_students_in" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_courses" ("COURSE");

ALTER TABLE "tables_responses" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_students" ("STUDENT");

ALTER TABLE "tables_responses" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_courses" ("COURSE");

ALTER TABLE "tables_responses" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_scenarios" ("SCENARIO");

ALTER TABLE "tables_responses" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_reflections_taken" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_responses" ("STUDENT");

ALTER TABLE "tables_reflections_taken" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_responses" ("COURSE");

ALTER TABLE "tables_reflections_taken" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_responses" ("SCENARIO");

ALTER TABLE "tables_reflections_taken" ADD FOREIGN KEY ("DATE_TAKEN") REFERENCES "tables_responses" ("DATE_TAKEN");

ALTER TABLE "tables_conversations_had" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_responses" ("STUDENT");

ALTER TABLE "tables_conversations_had" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_responses" ("COURSE");

ALTER TABLE "tables_conversations_had" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_responses" ("SCENARIO");

ALTER TABLE "tables_conversations_had" ADD FOREIGN KEY ("DATE_TAKEN") REFERENCES "tables_responses" ("DATE_TAKEN");

ALTER TABLE "tables_conversations_had" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "tables_stakeholders" ("STAKEHOLDER");

ALTER TABLE "tables_professors" ADD FOREIGN KEY ("PROFESSOR_id") REFERENCES "tables_scenarios" ("PROFESSOR_id");

ALTER TABLE "tables_stakeholders" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_scenarios" ("SCENARIO");

ALTER TABLE "tables_stakeholders" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "tables_coverage" ("STAKEHOLDER");

ALTER TABLE "tables_coverage" ADD FOREIGN KEY ("ISSUE") REFERENCES "tables_issues" ("ISSUE");

ALTER TABLE "tables_pages" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_scenarios" ("SCENARIO");

ALTER TABLE "tables_pages" ADD FOREIGN KEY ("NEXT_PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_conversations" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "tables_stakeholders" ("STAKEHOLDER");

ALTER TABLE "tables_reflection_questions" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_stakeholder_page" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_stakeholder_page" ADD FOREIGN KEY ("STAKEHOLDER") REFERENCES "tables_stakeholders" ("STAKEHOLDER");

ALTER TABLE "tables_generic_page" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_action_page" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_pages" ("PAGE");

ALTER TABLE "tables_actions_taken" ADD FOREIGN KEY ("RESPONSE") REFERENCES "tables_responses" ("RESPONSE");

ALTER TABLE "tables_actions_taken" ADD FOREIGN KEY ("ACTION_PAGE") REFERENCES "tables_action_page" ("id");

ALTER TABLE "tables_scenarios_for" ADD FOREIGN KEY ("COURSE") REFERENCES "tables_courses" ("COURSE");

ALTER TABLE "tables_scenarios_for" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_scenarios" ("SCENARIO");

ALTER TABLE "tables_scenarios_for" ADD FOREIGN KEY ("VERSION") REFERENCES "tables_scenarios" ("VERSION");

ALTER TABLE "tables_issues" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_scenarios" ("SCENARIO");

ALTER TABLE "tables_issues" ADD FOREIGN KEY ("VERSION") REFERENCES "tables_scenarios" ("VERSION");

ALTER TABLE "tables_students" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_assigned_to" ("STUDENT");

ALTER TABLE "tables_scenarios" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_assigned_to" ("SCENARIO");

ALTER TABLE "tables_scenarios" ADD FOREIGN KEY ("VERSION") REFERENCES "tables_assigned_to" ("VERSION");

ALTER TABLE "tables_students" ADD FOREIGN KEY ("STUDENT") REFERENCES "tables_student_times" ("STUDENT");

ALTER TABLE "tables_scenarios" ADD FOREIGN KEY ("SCENARIO") REFERENCES "tables_student_times" ("SCENARIO");

ALTER TABLE "tables_scenarios" ADD FOREIGN KEY ("VERSION") REFERENCES "tables_student_times" ("VERSION");

ALTER TABLE "tables_pages" ADD FOREIGN KEY ("PAGE") REFERENCES "tables_student_times" ("PAGE");

