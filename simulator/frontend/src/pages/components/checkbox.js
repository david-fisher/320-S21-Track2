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
import { PageContext } from '../simulator_window';
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
  const [choiceMade, setChoiceMade] = React.useState(undefined)

  useEffect (() => {
    fetch(`${BASE_URL}/get_page_info/?page_id=${props.pageId}`)
    .then(res => res.json())
    .then(actionData => {
      let actionChoices = []
      actionData.body.forEach(element => {
        let choice = {
          a_id: element.action_page_id,
          text: element.choice,
          result_page: element.result_page
        }
        actionChoices.push(choice)
      });
      setChoices(actionChoices)
    })
  }, [])

  useEffect (() => {
    //student id is the string "student" in the students api
    fetch(`${BASE_URL}/action_response/?student_id=${STUDENT_ID}&page_id=${props.pageNumber}&scenario_id=${props.match.params.sid}`)
    .then(res => res.json())
    .then(pageData => {
      console.log(pageData)
      setChoiceMade(pageData.choice)
    })
    .catch(err => {
      console.log(err)
    })
  }, [])


  const handleRadioChange = (event) => {
    setValue(event.target.value);
    setHelperText(' ');
    setError(false);
  };

  // const handleSubmit = (event) => {
  //   console.log("CLICKED")
  //   console.log(event);
  //   event.preventDefault();
  //   if (value !== '') {
  //     setHelperText('Good Answer!');
  //     setError(true);
  //     const resultPage = choices.filter(choice => choice.text === value)[0].result_page;
  //     event.update(props.activePage, resultPage);
  //     props.changePage(resultPage);
  //   } else {
  //     console.log("FAIL TO GO TO NEXT PAGE")
  //     setHelperText('Please select an option.');
  //     setError(true);
  //   }
  // };





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
    <PageContext.Consumer>
      {(context) => (
        <form onSubmit={(event) => {
          console.log("CLICKED");
          event.preventDefault();
          if (value !== '') {
            setHelperText('Good Answer!');
            setError(true);
            const selected = choices.filter(choice => choice.text === value)[0];
            console.log(selected)
            //student id is the string "student" in the students api
            fetch(BASE_URL + `/action_response/?action_page_id=${selected.a_id}&student_id=${STUDENT_ID}&scenario_id=${props.match.params.sid}&course_id=1`, {
              method: 'PUT',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                action_page: selected.a_id,
                reponse: value
              })
            })
            .then(res => res.json())
            .then(data => {
              console.log('Success:', data);
            })
            .catch((err) => {
              console.error("Error: ", err)
            })
            context.update(selected.result_page);
            props.changePage(selected.result_page);
          } else {
            console.log("FAIL TO GO TO NEXT PAGE")
            setHelperText('Please select an option.');
            setError(true);
          }
          
        }}>
          <FormControl component="fieldset" error={error} className={classes.formControl}>
            <RadioGroup aria-label="quiz" name="quiz" value={value} onChange={handleRadioChange}>
              {choices.map((choice, index) => (
                   (choiceMade === undefined) ?
                    <FormControlLabel value={choice.text} key={index} control={<Radio />} label={choice.text} />
                    :
                    <FormControlLabel value={choice.text} checked={choice.text === choiceMade} disabled={true} key={index} control={<Radio />} label={choice.text} />
                  
                ))
              }
            </RadioGroup>
            {choiceMade===undefined &&
            <div>
              <FormHelperText>{helperText}</FormHelperText>
              <Box width={100}>
                <SpecialButton type="save" title={nextPageTitle}></SpecialButton>
              </Box>
            </div>
            } 
          </FormControl>
        </form>
      )}
    </PageContext.Consumer>
  );
}

