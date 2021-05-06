import React from 'react';
import Introduction from './introduction';
import Reflection from './reflection';
import Action from './action';
import Stakeholders from './stakeholders'
import Feedback from './feedback'

function Page(props) {

    const pageTypes = {
        "G": (
            <Introduction 
                {...props}
            />),
        "I": (
            <Introduction 
                {...props}
            />),
        "S": (
            <Stakeholders 
                {...props}
            />),
        "A": (
            <Action
                {...props}
            />),
        "R": (
            <Reflection
                {...props}
            />),
        "F": (
            <Feedback
                {...props}
            />)

    };

    const { state, setState } = React.useState({
        visited: props.visited,
        completed: props.completed,
        pageNumber: props.pageNumber,
    });

    return (pageTypes[props.type]);
}

export default Page;

