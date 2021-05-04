import React, {useEffect, useState} from "react";
import PropTypes from 'prop-types'
import {
    withStyles,
    Typography,
    Box,
    Grid,
    Button,
    makeStyles,
  } from "@material-ui/core";
import HTMLRenderer from '../components/htmlRenderer'

const useStyles = makeStyles((theme) => ({
    videoBox: {
        margin: 'auto',
        maxWidth: '100%',
        maxHeight: '100%',
        
    },
}));

Sim_videoPlayer.defaulProps = {
    name: 'Please pass in a name for the video',
    description: 'Please pass in a description for the video'
}

Sim_videoPlayer.propTypes = {
    vid_url: PropTypes.string.isRequired,
    name: PropTypes.string,
    description: PropTypes.string,
}


export default function Sim_videoPlayer({vid_url, name, description}) {
    const [showVid, setShowVid] = useState(false);
    const classes = useStyles();
    return (
        <div>
            <Box paddingLeft={0} p={3}>
                <Button 
                    color="primary"
                    disableElevation
                    onClick={() => setShowVid(!showVid)}
                    size="medium"
                >
                    {showVid ? "hide video" : "show video"}
                </Button>
            </Box>
            {
                showVid && 
                <Grid container spacing={2} direction="row" justify="space-evenly" alignItems="stretch">
                    <Grid item xs={4}>
                        <iframe 
                            src={vid_url}
                            frameborder='0'
                            allow='autoplay; encrypted-media'
                            allowfullscreen='true'
                            title={name}
                            className={classes.videoBox}
                        />
                    </Grid>
                    <Grid item xs={8}>
                            <Typography variant="h6">
                                {name}
                            </Typography>
                            <HTMLRenderer html={description}/>
                    </Grid>
                </Grid>
            }  
        </div>
    );
}
