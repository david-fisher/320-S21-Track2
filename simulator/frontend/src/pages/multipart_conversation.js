import React, { useEffect, useState } from 'react';
import { FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, Typography } from '@material-ui/core';
import { BASE_URL, STUDENT_ID } from '../constants/config';

function MultipartConvo({ dialogue, match, page_id, stakeholder}) {

    const [ options, setOptions ] = useState([]);
    const [ chosenOptions, setChosenOptions ] = useState([]);
    const [ isLoading, setIsLoading ] = useState(true);

    useEffect(() => {
        let isMounted = true;
        fetchData();
        return () => {
            isMounted = false;
        }

        function fetchData() {
            setTimeout(() => {
                if(isMounted) {
                    setOptions(dialogue.map(option => {
                        return {
                            conversation: option.conversation,
                            question: option.question,
                            response: option.response,
                            stakeholder: option.stakeholder,
                        };
                    }));
                }
            }, 4000);
        }

    }, []);

    const getConvosHadData = async () => {
        const response = await fetch(`${BASE_URL}/conversations_had/?scenario_id=${match.params.sid}&student_id=${STUDENT_ID}&page_id=${page_id}`);
        
        if(!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        return data;
    }

    useEffect(() => {
        getConvosHadData().then(convoHadData => {

            const completedConvos = convoHadData.filter((convoHad) => {
                return convoHad.stakeholder === stakeholder.id;
            })
            .map((convo) => {
                console.log(convo.conversation);
                return {
                    conversation: convo.conversation[0].conversation,
                    question: convo.conversation[0].question,
                    response: convo.conversation[0].response,
                    stakeholder: convo.conversation[0].stakeholder
                }
            });

            setChosenOptions(completedConvos);

            console.log(options);

            setOptions(options.filter(option => {
                console.log(option);
                return !chosenOptions.some((chosen) => {
                    return chosen.conversation === option.conversation;
                })
            }));

            setIsLoading(false);
        });
    }, [])

    const sendConvoData = (convo) => {
        fetch(`${BASE_URL}/conversations_had/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "scenario_id": match.params.sid,
                "student_id": STUDENT_ID,
                "conversation_id": convo.conversation,
                "course_id": 1,
                "page_id": page_id
            })
        }).then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
        })
    };

    const handleChange = (event) => {
        const selectedOption = options[event.target.value];
        sendConvoData(selectedOption);
        setChosenOptions([...chosenOptions, selectedOption]);
        options.splice(event.target.value, 1)
        setOptions([...options]);;
    };

    return (
        <div id="convos">
            <FormControl component="fieldset">
                <FormLabel component="legend">Questions to ask...</FormLabel>
                <RadioGroup aria-label="options" name="questions1" onChange={handleChange}>
                    {!isLoading && options.filter(option => {
                        return !chosenOptions.some((chosen) => {
                            return chosen.conversation === option.conversation;
                        })}).map((option, index) => {
                        return (
                            <FormControlLabel value={index} control={<Radio />} label={option.question}></FormControlLabel>
                        );
                    })}
                </RadioGroup>
            </FormControl>
                {!isLoading &&
                    chosenOptions.map((option) => {
                        const you = `You: ${option.question}`;
                        const them = `Them: ${option.response}`;
                        return (
                            <div>
                                <Typography>{you}</Typography>
                                <Typography>{them}</Typography>
                            </div>
                        );
                    })
                }
        </div>

    );
    

}

export default MultipartConvo;