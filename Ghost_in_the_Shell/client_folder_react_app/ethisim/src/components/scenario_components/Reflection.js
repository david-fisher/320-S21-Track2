import React, { useState } from 'react';
import Body from '../Body';
import Title from '../Title';
import VersionControl from '../VersionControl';
import { Typography, Container } from '@material-ui/core';
import QuestionFields from '../QuestionComponent/questions';
import { mockReflectionHistory } from '../../shared/mockScenarioData';

export default function Reflection(props) {
    //const titleData = mockActionComponent.title;
    //const bodyData = mockActionComponent.body;
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');

    return (
        <Container component="main">
            <Typography align="center" variant="h2">
                Reflection Component
            </Typography>
            <VersionControl
                history={mockReflectionHistory.history}
                type={mockReflectionHistory.type}
                setTitle={setTitle}
                setBody={setBody}
            />
            <Title title={title} />
            <Body body={body} />
            <QuestionFields />
        </Container>
    );
}
