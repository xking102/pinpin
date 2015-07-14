var React = require("react");
var AMUIReact = require('amazeui-react');
var {ScrollSpy,Grid,Col,Panel} = AMUIReact;

var mui = require('material-ui');
var {Card, CardMedia, CardTitle, CardText, Paper} = mui;

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
		var group = this.props.group;
		var detail_link = '#/group/'+group.id;
        var title = group.title;
        if(title){
            if(title.length>8){
                title = title.substring(0,8)+'...';
            }
        }
		return(
            <div>
            <a href={detail_link}>
			<div className="span3"
                style={{marginBottom:'20px',marginRight:'20px'}}
                onMouseEnter={this.MouseIn} onMouseLeave={this.MouseOut}>

            <Paper zDepth={this.state.depth}>
            <ScrollSpy norepeat animation="slide-bottom" delay={this.props.delay}>

                <Card>
                    <CardMedia overlay={
                        <CardTitle title={title} />
                    }>
                        <img  src={group.image+'.small.jpg'}/>
                    </CardMedia>

                    <CardText>
                        <p>到手价：￥ {group.unit_price}</p>
                        <p>剩余数量：{group.total_qty-group.req_qty-group.confirm_qty}</p>
                        <p>发布时间：{group.create_dt}</p>
                    </CardText>
                </Card>


            </ScrollSpy>
            </Paper>
			</div>
            </a>
            </div>

		)
	},

})
