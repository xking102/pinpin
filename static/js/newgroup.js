var React = require('react');


var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {TextField, Paper, RaisedButton} = mui;
var Dropzone = require('react-dropzone');
var LoadingMask = require("./Components/LoadingMask");

injectTapEventPlugin();
var App = React.createClass({
  childContextTypes: {
    muiTheme: React.PropTypes.object
  },
  getChildContext: function() {
    return {
      muiTheme: ThemeManager.getCurrentTheme()
    };
  },
  _checkField:function(){
    var title = this.refs.title.getValue();
    var desc = this.refs.desc.getValue();
    var errorImages = this.state.errorImages;
    var errorPrice = this.state.errorPrice;
    var errorQty = this.state.errorQty;

    if(title.length==0||desc.length==0||errorImages.length>0||errorPrice.length>0||errorQty.length>0){
      this.setState({
        errorSubmit:'请填写完整'
      });
      return true;
    }else{
      this.setState({
        errorSubmit:''
      });
      return false;
    }
  },
  PostGroup:function(num){
    if(num){
      return '';
    }
    this.setState({
      submitflag:true
    });
    this.refs.loading.show();
    var formData = new FormData();
    for (var i=0;i<this.state.images.length;i++){
      var file = this.state.images[i];
      formData.append('photos',file);
    }
    formData.append('images',this.state.images);
    formData.append('title',this.refs.title.getValue());
    formData.append('desc',this.refs.desc.getValue());
    formData.append('unit_price',this.refs.price.getValue());
    formData.append('list_price',0);
    formData.append('total_qty',this.refs.qty.getValue());
    $.ajax({
      url      : '/api/v1/groups',
      type     : 'POST',
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      data:formData,
      success: function(resp) {
        console.log('succ');
        this.refs.loading.dismiss();
        this.setState({
          submitflag:false
        });
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
        this.refs.loading.dismiss();
      }.bind(this)
    });
  },
  getInitialState:function(){
    return {
      images:[],
      color:[],
      size:[],
      other:[],
      flag:true,
      errorImages:'别忘了上传图片',
      errorSubmit:'',
      submitflag:false
    }
  },
  _handleForm:function(e){
    e.preventDefault();
    var num = this._checkField();
    this.PostGroup(num);


  },
  render: function () {
    var showSubmitError = this.state.errorSubmit.length==0?'':
    <div style={{marginTop:'50px'}} className="alert alert-error">{this.state.errorSubmit}</div>;
    return (
      <div style={{marginLeft:'20%',marginRight:'20%'}}  >
          <Paper zDepth={3}>
          <div style={{marginLeft:'10px',marginRight:'10px',paddingBottom:'20px'}}>



          <form onSubmit={this._handleForm} ref="addGroupForm" name="addGroup" encType="multipart/form-data" method="POST">
            <TextField
              ref="title"
              style={{width:'100%'}}
              hintText="商品名称"
              type='text'
              multiLine={true}
              floatingLabelText="输入商品名称"
            />

            <br/>

            <TextField
              ref="desc"
              style={{width:'100%'}}
              hintText="商品详情介绍"
              type='text'
              multiLine={true}
              floatingLabelText="输入商品详情介绍"
            />

            <br/>

            <TextField
              ref="price"
              hintText="到手单价"
              floatingLabelText="输入到手单价"
              errorText={this.state.errorPrice}
              onChange={this._handleErrorPrice}
            />

            &nbsp;

            <TextField
              ref="qty"
              hintText="团购数量"
              floatingLabelText="输入本次团购数量"
              errorText={this.state.errorQty}
              onChange={this._handleErrorQty}
            />

            <br/>
            <br/>
            <br/>

            <Dropzone ref="dropzone" onDrop={this._onDrop} size={150} >
              <div>你可以拖拽多张图片到此处或者双击选择多张图片</div>
            </Dropzone>
            {this.showFiles()}

            <br/>


            <div className="pull-right">
            <a className="btn btn-link" onClick={this._onHandleCancel}>重新填写</a>
            &nbsp;
            <RaisedButton
            label="添加"
            secondary={true}
            disabled={this.state.submitflag}
            />
            </div>

            {showSubmitError}


          </form>


          </div>
          </Paper>
          <LoadingMask ref="loading"/>
      </div>
    );
  },


  _onDrop:function(imgs){
    if(imgs.length<6){
      this.setState({
        images:imgs,
        errorImages:''
      });
    }else{
      this.setState({
        images:'',
        errorImages:'至多可以上传5张图片'
      });
    }
  },

  showFiles: function () {
    if (this.state.images.length <= 0) {
      return <div style={{marginTop:'10px'}} className="alert alert-error">{this.state.errorImages}</div>;
    }

    var images = this.state.images;

    return (
      <div>
        <h3>预览</h3>
          {[].map.call(images, function (f, i) {
            return <img style={{marginRight:'3px',marginBottom:'3px'}}width={100} height={100} key={i} src={f.preview} />;
          })}
      </div>
    );
  },



  _onHandleCancel:function(){
    this.refs.addGroupForm.getDOMNode().reset();
  },

  _handleErrorPrice:function(){
    if(this.refs.price.getValue()>0){
      this.setState({
        errorPrice:''
      });
    }else{
      this.setState({
        errorPrice:'请输入大于0的数字'
      })
    }
  },


  _handleErrorQty:function(){
    var num = this.refs.qty.getValue();
    if(num>0&&num%1==0){
      this.setState({
        errorQty:''
      });
    }else{
      this.setState({
        errorQty:'请输入大于0的整数'
      })
    }
  },

});




var mainCom = React.render(
  <App />,
  document.getElementById('app')
)
