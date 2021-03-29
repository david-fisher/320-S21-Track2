import React from 'react';
import Introduction from './introduction';
import Reflection from './reflection';
import Action from './action';
import Stakeholders from './stakeholders'

export default class Page {
    constructor(visited, completed, pageNumber, type, nextPageNumber=1, title, content) {
        const pageTypes = {
            "A": (
                <Action 
                    nextPageID={nextPageNumber}
                    prevPageID={pageNumber - 1}
                    content={content}        
                />),
            "G": (
                <Introduction 
                    nextPageNumber={nextPageNumber}
                    prevPageNumber={pageNumber - 1}
                    content={content}
                />),
            "I": (
                <Introduction 
                    nextPageNumber={nextPageNumber}
                    content={content}
                />),
            "R": (
                <Reflection 
                    nextPageID={nextPageNumber}
                    prevPageID={pageNumber - 1}
                    content={content}
                />),
            "S": (
                <Stakeholders 
                    nextPageID={nextPageNumber}
                    prevPageID={pageNumber - 1}
                    content={content}
                />)
        }

        this.visited = visited;
        this.completed = completed;
        this.pageNumber = pageNumber;
        this.title = title;
        this.html = (pageTypes[type]);
    }
}