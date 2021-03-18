import React, {useEffect, useState} from "react";
import PropTypes from 'prop-types'
import AudioPlayer from './AudioPlayer'
import {
    withStyles,
    Typography,
    Box,
    Grid,
    Button,
    makeStyles,
  } from "@material-ui/core";
import HTMLRenderer from './htmlRenderer'

const useStyles = makeStyles((theme) => ({
    ytBox: {
        margin: 'auto',
        width: '100%',
        height: '130%',
    },
    full: {
        margin: 'auto',
        width: '100%',
        height: '100%',
    }
}));

MultiMedia.defaulProps = {
    name: '',
    description: '',
    height: 300, 
    type: '',
}

MultiMedia.propTypes = {
    source: PropTypes.string.isRequired,
    name: PropTypes.string,
    description: PropTypes.string,
}


export default function MultiMedia({source, name, description, height, type}) {
    const [showContent, setShowContent] = useState(false);
    const classes = useStyles();
    return (
        <div>
            <Box paddingLeft={0} p={3}>
                <Button 
                    color="primary"
                    disableElevation
                    onClick={() => setShowContent(!showContent)}
                    size="medium"
                >
                    {showContent ? `hide ${type}` : `show ${type}`}
                </Button>
            </Box>
            {
                showContent && 
                <Box height={height}>
                    <Grid container spacing={2} direction="row" justify="space-between" alignItems="stretch">
                        <Grid item xs={5}>
                            {
                                (type === 'link' &&
                                <iframe 
                                    src={source}
                                    frameborder='0'
                                    allow='autoplay; encrypted-media'
                                    allowfullscreen='true'
                                    title={name}
                                    className={classes.ytBox}
                                />)
                                ||
                                (type === 'video' &&
                                <video className={classes.full} controls >
                                    <source src={source} type="video/mp4"/>
                                </video>
                                )
                                ||
                                (type === 'image' &&
                                <img src={source} className={classes.full}/>
                                )
                                ||
                                (type === 'audio' &&
                                        <AudioPlayer source={source} />
                                )
                            }
                        </Grid>
                        <Grid item xs={6}>
                                <Typography variant="h6">
                                    {name}
                                </Typography>
                                <HTMLRenderer html={description}/>
                        </Grid>
                    </Grid>
                </Box>
            }  
        </div>
    );
}
