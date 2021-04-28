import React, { useEffect, useState } from 'react';
import { FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, Typography } from '@material-ui/core';

function Options(props) {

    const [ unselectedOptions, setUnselectedOptions ] = useState([]);
    const [ selectedOptions, setSelectedOptions ] = useState([]);
    const [ response, setResponse ] = useState({});

    const handleChange = (event) => {
        const selectedOption = props.options[event.value];
        props.setChosenOptions([...props.chosenOptions, selectedOption]);
        props.setOptions(props.options.splice(event.value, 1));
    };


    return (
        <div id="convo">
            <FormControl component="fieldset">
                <FormLabel component="legend">Questions to ask...</FormLabel>
                <RadioGroup aria-label="options" name="questions1" onChange={handleChange}>
                    {props.options.map((option, index) => {
                        return (
                            <FormControlLabel value={index} control={<Radio />} label={option.question}></FormControlLabel>
                        );
                    })}
                </RadioGroup>
            </FormControl>
        </div>
    );

}

function MultipartConvo(props) {

    const [ options, setOptions ] = useState([]);
    const [ chosenOptions, setChosenOptions ] = useState([]);

    useEffect(() => {
        console.log(props);
        setOptions(props.dialogue.map(option => {
            return {
                question: option.question,
                response: option.response
            };
        }));
    }, []);

    return (
        <div id="convos">
            <Options options={options} setOptions={setOptions} chosenOptions={chosenOptions} setChosenOptions={setChosenOptions}>
            </Options>
            <Typography>
                {() => {
                    chosenOptions.map((option) => {
                        return `You: ${options.question}\n\tThem:${options.response}`;
                    });
                }}
            </Typography>
        </div>

    );
    

}

export default MultipartConvo;