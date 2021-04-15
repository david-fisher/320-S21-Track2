import React,{useEffect} from "react";
import { makeStyles } from '@material-ui/core/styles';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import FormHelperText from '@material-ui/core/FormHelperText';
import {Box, Button} from "@material-ui/core";
import SpecialButton from "./SpecialButton"

import { BASE_URL, STUDENT_ID, SCENARIO_ID } from "../../constants/config";
import axios from 'axios';
import { ScenariosContext } from "../../Nav";
import { TrainOutlined, TrainRounded } from "@material-ui/icons";

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(3),
  },
  button: {
    margin: theme.spacing(1, 1, 0, 0),
  },
}));

export default function ErrorRadios(props) 
{
  let nextPageTitle = "";
  let content_url = '/pages';
  const classes = useStyles();
  const [value, setValue] = React.useState('');
  const [error, setError] = React.useState(false);
  const [helperText, setHelperText] = React.useState('Choose carefully');
  const [scenarios, setScenarios] = React.useContext(ScenariosContext);
  const [choices, setChoices] = React.useState([]);

  useEffect (() => {
    fetch(`${BASE_URL}/get_page_info?page_id=${props.page_id}`)
    .then(res => res.json())
    .then(actionData => {
      let actionChoices = []
      
      actionData.results.filter(element => element.page === props.pageNumber).
      forEach(element => {
        let choice = {
          text: element.choice,
          result_page: element.result_page
        }
        actionChoices.push(choice)
      });
      console.log(actionChoices)
      setChoices(actionChoices)
    })
  }, [])

  const handleRadioChange = (event) => {
    setValue(event.target.value);
    setHelperText(' ');
    setError(false);
  };

  const handleSubmit = (event) => {
    console.log("CLICKED")
    event.preventDefault();
    if (value !== '') {
      setHelperText('Good Answer!');
      setError(true);
      props.changePage(choices.filter(choice => choice.text === value)[0].result_page)
    } else {
      console.log("FAIL TO GO TO NEXT PAGE")
      setHelperText('Please select an option.');
      setError(true);
    }
  };





  // useEffect(() => {
  //   // backend call
  //   console.log("base: " + BASE_URL + " scenario: " + SCENARIO_ID + " student: " + STUDENT_ID);
  //   axios({
  //     method: 'get',
  //     url: BASE_URL + content_url,
  //     headers: {
  //       scenarioID: scenarios.currentScenarioID,
  //       studentID: STUDENT_ID,
  //     }
  //   }).then(response => {
  //     console.log(response);

  //     const x = [];
  //     console.log(content_url);
  //     if (scenarios.currentScenarioID == 1)
  //     {
  //       for (var i = 0; i < response.data[0].option.length; i++)
  //         x.push({value:response.data[0].option_id[i], label: response.data[0].option[i]});
  //       console.log(x);
  //       setChoices(choices => x);
  //     }
  //     if ((scenarios.currentScenarioID == 2)){
  //       for (var i = 0; i < response.data[1].option.length; i++)
  //         x.push({value:response.data[1].option_id[i], label: response.data[1].option[i]});
  //       console.log(x);
  //       setChoices(choices => x);
  //     }
  //   }).catch((err)=>{
  //     console.log("err",err);
  //     //alert(err);
  //   });
  // }, [scenarios])

  // function getNextPageTitle(props) {
  //   switch (props.nextPageName) {
  //     case "gatheredInformation": nextPageTitle = "Gathered Information";
  //     break;
  //     case "summary": nextPageTitle = "Summary";
  //     break;
  //     default:
  //       break;
  //   }
  // }
  // getNextPageTitle(props);

  return (
    <form onSubmit={handleSubmit}>
      <FormControl component="fieldset" error={error} className={classes.formControl}>
        <RadioGroup aria-label="quiz" name="quiz" value={value} onChange={handleRadioChange}>
          {choices.map((choice, index) => (
              <FormControlLabel value={choice.text} key={index} control={<Radio />} label={choice.text} />
            ))
          }
        </RadioGroup>
        <FormHelperText>{helperText}</FormHelperText>
        <Box width={100}>
          <SpecialButton type="save" title={nextPageTitle}></SpecialButton>
        </Box>
      </FormControl>
    </form>
  );
}

