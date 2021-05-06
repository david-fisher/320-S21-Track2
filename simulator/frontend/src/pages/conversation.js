import React, { useState, useContext, useEffect } from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  Button,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL } from "../constants/config";
import { ScenariosContext } from "../Nav";
import MultipartConvo from './multipart_conversation';

const TextTypography = withStyles({
  root: {
    color: "#373a3c",
    whiteSpace: "pre-line",
  },
})(Typography);

const useStyles = makeStyles((theme) => ({
  textBox: {
    overflowY: "auto",
    maxHeight: window.innerHeight * 0.6,
    marginTop: theme.spacing(4),
    borderRadius: "5px",
    boxShadow: "0px 0px 2px",
  },
}));

function Conversation(props) {

  function goToStakeholders() {
    props.setShowStakeholders(true);
  }

  const [monologue, setMonologue] = useState('');
  const [ dialogue, setDialogue ] = useState({});
  const [ isLoading, setIsLoading ] = useState(true);
  const [scenarios, setScenarios] = useContext(ScenariosContext);

  const getConversationData = async () => {

    const response = await fetch(`${BASE_URL}/stakeholder_conv/?stakeholder_id=${props.stakeholder.id}`);

    if(!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  };

  const setConversation = (conversation) => {

    let data = conversation.map((convo) => {
      return {
        conversation: convo.conversation,
        question: convo.question,
        response: convo.response
      };
    });

    setDialogue(data);

  };

  useEffect(() => {

    getConversationData().then(conversationData => {

      setConversation(conversationData);
      setIsLoading(false)

    })
    .catch(err => {
      alert(err);
    });

  }, [scenarios]);

  const classes = useStyles();

  return (
    <div>
      <Box mt={5}>
        <Grid container direction="row" justify="center" alignItems="center">
          <TextTypography variant="h4" align="center" gutterBottom>
            {props.stakeholder.name}
          </TextTypography>
        </Grid>
      </Box>
      <Grid item style={{ marginLeft: "0rem", marginTop: "-3rem" }}>
        <Button
          variant="contained"
          disableElevation
          color="primary"
          onClick={goToStakeholders}
          >
          Return
            </Button>
      </Grid>
      <Grid container direction="row" justify="space-between">
        <Grid
          item
          style={{
            marginLeft: "0rem",
            marginRight: "0rem",
            marginTop: "-3rem",
          }}
        >
        </Grid>
      </Grid>
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box p={10} className={classes.textBox}>
              {!isLoading ?
              <MultipartConvo dialogue={dialogue} page_id={props.page_id} match={props.match} stakeholder={props.stakeholder}/> 
              : <Typography>One second while things are loading...</Typography> }
          </Box>
        </Grid>
      </Grid>
    </div>
  );
}

export default Conversation;