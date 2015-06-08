var React = require("react");

var mui = require('material-ui');
var {Paper} = mui;

var GroupItemNumDesc = require("./GroupItemNumDesc");
var GroupItemActions = require('./GroupItemActions');

module.exports = React.createClass({
    getInitialState:function(){
        return {
            depth:3
        }
    },
    MouseIn:function(){
        this.setState({
            depth:1
        });
    },
    MouseOut:function(){
        this.setState({
            depth:3
        });
    },
    render:function(){
		return(
			<div style={{marginBottom:'15px'}} onMouseEnter={this.MouseIn} onMouseLeave={this.MouseOut}>
                <Paper zDepth={this.state.depth}>
                    <div className="row-fluid" style={{marginLeft:'10px',paddingTop:'10px'}}>
                        <span>{this.props.group.title}</span>
                        <span className="pull-right" style={{marginRight:'2%'}}>{this.props.group.create_dt}</span>
                    </div>

                    <div className="row-fluid" style={{marginLeft:'10px',paddingBottom:'10px'}}>
                        <div className="span4">
                        <img alt="221x125" src="/static/imgs/groups/221x125.gif" />
                        </div>
                        
                        <div className="span4">
                        <GroupItemNumDesc group={this.props.group} />
                        </div>

                        <div className="span4">
                        <GroupItemActions group={this.props.group} 
                            listGroups={this.props.listGroups}
                            changeGroupStatus={this.props.changeGroupStatus} />
                        </div>
                    </div>
                </Paper>
            </div>

		)		
	}
})