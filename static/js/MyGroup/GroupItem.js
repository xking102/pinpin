var React = require("react");

var mui = require('material-ui');
var {Paper} = mui;

var GroupItemNumDesc = require("./GroupItemNumDesc");
var GroupItemActions = require('./GroupItemActions');

module.exports = React.createClass({
    getInitialState:function(){
        return {
            depth:1
        }
    },
    MouseIn:function(){
        this.setState({
            depth:3
        });
    },
    MouseOut:function(){
        this.setState({
            depth:1
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
                        <img style={{width:'250px',height:'150px'}} src={this.props.group.image+".big.png"} />
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
