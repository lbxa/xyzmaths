import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { notesLoader } from "./lib/notes-loader";
import { createNoteRenderer } from "./lib/note-markdown.mjs";
import { weeklyProblemLoader } from "./lib/weekly-problem-loader";

const renderProblemText = createNoteRenderer();

export const collections = {
  weeklyProblems: defineCollection({
    loader: weeklyProblemLoader,
    schema: z.object({
      title: z.string().trim().min(1),
      description: z.string().trim().min(1),
      date: z.coerce.date(),
      source: z.url(),
      sourceLabel: z.string().trim().min(1),
      topic: z.string().trim().min(1),
      difficulty: z.number().int().min(1).max(10),
      estimatedTime: z.number().int().positive(),
      statement: z.string().trim().min(1),
      solution: z.string().trim().min(1),
      referenceCode: z.string().min(1).optional(),
    }).transform(({ statement, solution, ...metadata }) => ({
      ...metadata,
      statementHtml: renderProblemText(statement),
      solutionHtml: renderProblemText(solution),
    })),
  }),
  bookPages: defineCollection({
    loader: notesLoader("pages"),
    schema: z.object({
      book: z.string(), title: z.string(), group: z.string(), order: z.number().int(),
      part: z.string().optional(), printPage: z.string().optional(),
      outline: z.array(z.object({
        id: z.string(), title: z.string(), level: z.number().int().min(2).max(6).default(2),
      })),
    }),
  }),
  bookExercises: defineCollection({
    loader: notesLoader("exercises"),
    schema: z.object({
      book: z.string(),
      key: z.string(), source: z.string(), number: z.string(), title: z.string(),
      assignment: z.string().nullable(), question: z.number().int().nullable(),
      statementPage: z.string(), solutionPage: z.string(), solution: z.string(), solutionMarkdown: z.string(),
    }),
  }),
  bookFigures: defineCollection({
    loader: notesLoader("figures"),
    schema: z.object({ content: z.string() }),
  }),
};
