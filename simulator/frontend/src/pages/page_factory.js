import React from 'react';
import Introduction from './introduction';
import Reflection from './reflection';
import Action from './action';
import Stakeholders from './stakeholders'

export default class Page {
    constructor(visited, completed, pageNumber, type, nextPageNumber=1, prevPageNumber=1, content) {
        const pageTypes = {
            "A": (
                <Action 
                    nextPageID={nextPageNumber}
                    prevPageID={prevPageNumber}
                    content={content}        
                />),
            "G": (
                <Introduction 
                    nextPageNumber={nextPageNumber}
                    prevPageNumber={prevPageNumber}
                    content={content}
                />),
            "I": (
                <Introduction 
                    nextPageNumber={nextPageNumber}
                    prevPageNumber={prevPageNumber}
                    content={content}
                />),
            "R": (
                <Reflection 
                    nextPageID={nextPageNumber}
                    prevPageID={prevPageNumber}
                    content={content}
                />),
            "S": (
                <Stakeholders 
                    nextPageID={nextPageNumber}
                    prevPageID={prevPageNumber}
                    content={content}
                />)
        }

        this.visited = visited;
        this.completed = completed;
        this.pageNumber = pageNumber;
        this.html = (pageTypes[type]);
    }
}